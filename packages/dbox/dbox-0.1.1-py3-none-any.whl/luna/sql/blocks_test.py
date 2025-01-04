from typing import ClassVar

import pytest
from pydantic import computed_field

from .base import AbstractSqlBlock, PredefinedTemplateSqlBlock, SqlGenContext
from .blocks import HashData, SelectBlock, SqlQuery, SqlTarget, StackBlock


def test_jinja2_block(ctx: SqlGenContext):
    class TestBlock0(PredefinedTemplateSqlBlock):
        template_name: ClassVar[str] = "tests/test0.j2"

        a: int = 1

        @computed_field
        def b(self) -> int:
            return self.a + 1

    block = TestBlock0(a=1)
    assert block.to_sql(ctx) == "select 1 as a, 2 as b"


@pytest.mark.parametrize(
    "input_block",
    [SqlQuery(sql="select 1 as a, 2 as b"), SqlTarget(target="`project.dataset.table`")],
)
def test_hash_data(ctx: SqlGenContext, input_block: AbstractSqlBlock):
    block = HashData(input_block=input_block)
    query = block.to_sql(ctx)
    print(query)


def test_select_block(ctx: SqlGenContext):
    source = SqlQuery(sql="select 1 as a, 2 as b")
    source.to_sql(ctx)
    apply1 = SelectBlock(
        selects=[
            "a",
            "b",
        ],
        filters=["b > 1"],
    )
    query = apply1(source).to_sql(ctx)
    print(query)


def test_stack_block(ctx: SqlGenContext):
    blocks = [
        SqlQuery(sql="select 1 as a, 2 as b"),
        SelectBlock(
            selects=[
                "a",
                "b",
            ],
            filters=["b > 1"],
        ),
        HashData(),
    ]
    block = StackBlock(blocks=blocks)
    query = block.to_sql(ctx)
    print(query)
