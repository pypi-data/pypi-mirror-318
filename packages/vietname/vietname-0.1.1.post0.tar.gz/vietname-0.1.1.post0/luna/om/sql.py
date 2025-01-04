from typing import ClassVar, List, Optional, Type

from pydantic import Field

from luna.sql.base import AbstractSqlBlock, PredefinedTemplateSqlBlock, SqlField
from luna.sql.blocks import SelectBlock, SqlTarget
from luna.sql.join import JoinBlock, JoinTarget

from .model import DModel


class PagingBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "paging.sql"

    order_by: List[str] = Field(default_factory=list)
    limit: Optional[int] = None
    offset: Optional[int] = None


class CountBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "count.sql"


class InsertBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "insert.sql"

    model: Type[DModel]
    columns: List[str]
    pk_col: str


class UpdateBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "update.sql"

    model: Type[DModel]
    pk_col: str
    columns: List[str]


class SoftDelete(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "soft_delete.sql"

    model: Type[DModel]
    pk_col: str


class Delete(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "delete.sql"

    model: Type[DModel]


class DModelRelation(AbstractSqlBlock):
    model: Type[DModel]

    def model_post_init(self, __context):
        self.name = self.model.__tablename__

    def to_sql(self, ctx=None):
        return SelectBlock(
            input_block=SqlTarget(target=self.model.get_fqtn()), selects=self.model.self_fields()
        ).to_sql()

    def sql_target(self, ctx):
        return self.model.get_fqtn()

    def get_fields(self):
        return [SqlField(name=f) for f in self.model.self_fields()]


def join_models(base: Type[DModel], *args):
    targets = []
    for model, condition in args:
        targets.append(JoinTarget(target=DModelRelation(model=model), condition=condition))
    join = JoinBlock(base=DModelRelation(model=base), joins=targets)
    return join.to_sql()
