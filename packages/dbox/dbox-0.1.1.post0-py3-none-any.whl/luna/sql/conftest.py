import pytest

from luna.ctx import set_context
from luna.sql.ctx import SqlGenContext


@pytest.fixture(scope="package")
def ctx():
    sql_ctx = SqlGenContext()
    with set_context(sql=sql_ctx):
        yield sql_ctx
