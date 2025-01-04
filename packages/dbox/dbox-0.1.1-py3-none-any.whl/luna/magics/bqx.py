from __future__ import print_function

import logging
import shlex
from functools import cached_property, lru_cache
from typing import List, Optional

import duckdb
import IPython
import polars as pl
from google.auth.credentials import Credentials
from google.cloud import bigquery
from humanfriendly import format_size
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.magic_arguments import MagicArgumentParser
from pydantic import BaseModel, ConfigDict, Field, field_validator

from luna.sql.base import SqlGenContext
from luna.utils.bigquery.downloader import BigQueryDownloader
from luna.utils.bigquery.tracker import ProgressTracker, TqdmTracker

log = logging.getLogger(__name__)

count = 0
bqlparser = MagicArgumentParser()
bqlparser.add_argument("--max-rows", "-n", type=int, default=None)
bqlparser.add_argument("--copy", "-c", action="store_true", default=False)


class MagicsContext(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    dest_table: Optional[str] = None
    duckdb_conn: Optional[duckdb.DuckDBPyConnection] = None
    project: Optional[str] = None
    dataset: Optional[str] = None
    credentials: Optional[Credentials] = None
    tracker: ProgressTracker = TqdmTracker(tqdm_type="std")

    max_rows: Optional[int] = None
    filter: Optional[str] = None
    exclude_fields: Optional[List[str]] = Field(default=None)
    exclude_tagged_columns: bool = False
    include_fields: Optional[List[str]] = None
    # query
    dry_run: bool = False

    # copy
    max_rows_copy: int = 2 << 10
    copy_separator: str = ","

    @field_validator("exclude_fields", "include_fields", mode="before")
    @classmethod
    def to_list(cls, v: str):
        if v is None:
            return None
        return [e.strip() for e in v.split(",")]

    @field_validator("dry_run", "exclude_tagged_columns", mode="before")
    @classmethod
    def to_bool(cls, v: str):
        if v is None:
            return False
        if isinstance(v, bool):
            return v
        return v.lower() in ("true", "yes", "1")

    @cached_property
    def bqclient(self):
        return _create_bqclient(self.project, self.credentials)

    @cached_property
    def bqdownloader(self):
        return _create_bqdownloader(self.bqclient, self.tracker)

    @cached_property
    def j2(self):
        return SqlGenContext().jinja

    def update(self, **kwargs):
        data = self.model_dump()
        for k in kwargs:
            if k not in data:
                raise ValueError(f"Unknown directive: {k}")
        data.update(kwargs)
        return MagicsContext(**data)

    def run_query(self, sql_query: str):
        # a query
        bqjob = None
        query_lowercase = sql_query.lower()
        if " " not in query_lowercase.strip():
            # must be a table reference
            table = self.bqclient.get_table(sql_query.strip())

        else:
            # a sql query
            config = bigquery.QueryJobConfig(dry_run=self.dry_run)
            try:
                bqjob = self.bqclient.query(sql_query, job_config=config)
                bqjob.result()
            except Exception as e:
                log.error("Query failed: %s", e)
                return

            log.info(
                "Query: [%s] - total billed %s - total processed %s",
                bqjob.job_id,
                format_size(bqjob.total_bytes_billed),
                format_size(bqjob.total_bytes_processed),
            )
            if self.dry_run:
                log.info("Dry run query completed.")
                return None
            table = bqjob.destination
        if self.max_rows is None:
            max_rows = 2 << 10
            log.warning(
                "No max-rows specified, using default value: %d. Set max-rows to 0 to explicitly download all rows.",
                max_rows,
            )
            self.max_rows = max_rows
        # download the table
        table: bigquery.Table = self.bqclient.get_table(table)

        def select_fields(fields: List[bigquery.SchemaField]):
            if self.include_fields:
                return [e.name for e in fields if e.name in self.include_fields]
            if self.exclude_fields:
                return [e.name for e in fields if e.name not in self.exclude_fields]
            if self.exclude_tagged_columns:
                return [e.name for e in fields if not e.policy_tags]
            return [e.name for e in fields]

        arrow_table = self.bqdownloader.download_table(
            table,
            max_rows=self.max_rows,
            row_restriction=self.filter,
            select_fields=select_fields,
        )
        df = pl.from_arrow(arrow_table)
        return df, bqjob


@lru_cache(maxsize=32)
def _create_bqclient(project: str, credentials: Credentials):
    log.debug("Creating bqclient for project %s", project)
    return bigquery.Client(project=project, credentials=credentials)


@lru_cache(maxsize=32)
def _create_bqdownloader(bqclient: bigquery.Client, tracker: ProgressTracker):
    return BigQueryDownloader(bqclient=bqclient, tracker=tracker)


default_ctx = MagicsContext()


def bqx_magic(line, content: str):
    ctx = default_ctx.model_copy()
    global count  # noqa: PLW0603
    count += 1

    args = vars(bqlparser.parse_args(shlex.split(line)))
    if args["max_rows"] is not None:
        ctx.max_rows = int(args["max_rows"])

    ipy: InteractiveShell = IPython.get_ipython()
    directives = {}
    query_lines = []
    for line in content.splitlines():
        if line.strip().startswith("--") or line.strip().startswith("###"):
            continue  # ignore comment
        if line.strip().startswith("#") and "=" in line:
            k, v = line.strip().lstrip("# ").split("=", 1)
            k, v = k.strip(), v.strip()
            k = k.replace("-", "_")
            directives[k] = v
        else:
            query_lines.append(line)
    sql_query = "\n".join(query_lines)

    # aliases
    for k, v in {
        "exclude": "exclude_fields",
        "include": "include_fields",
        "dest": "dest_table",
        "n": "max_rows",
        "dry-run": "dry_run",
        "no-tagged": "exclude_tagged_columns",
    }.items():
        if k in directives:
            directives[v] = directives.pop(k)
    log.debug("Using directives: %s", directives)
    ctx = ctx.update(**directives)

    sql_query = ctx.j2.from_string(sql_query).render(ipy.ns_table["user_global"]).strip()
    log.debug("Using context: %s", ctx)
    ret = ctx.run_query(sql_query)
    if ret is None:
        return None
    else:
        df, bqjob = ret
    result_name = "b%d" % count
    bqjob_name = "bq%d" % count
    ipy.push({result_name: df, bqjob_name: bqjob})
    log.info("Stored result into %s.", result_name)
    if args["copy"]:
        df.slice(0, ctx.max_rows_copy).write_clipboard(separator=ctx.copy_separator)
    if ctx.duckdb_conn is not None:
        ctx.duckdb_conn.sql(f"CREATE OR REPLACE TEMP TABLE {result_name} AS SELECT * FROM df")
        if ctx.dest_table:
            ipy.push({ctx.dest_table: df})
            ctx.duckdb_conn.sql(f"CREATE OR REPLACE TABLE {ctx.dest_table} AS SELECT * FROM df")
        duck_relation = ctx.duckdb_conn.table(result_name)
        return duck_relation
    return df
