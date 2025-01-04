from pathlib import Path
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .ctx import SqlGenContext, use_sql_context

parent_dir = Path(__file__).parent


class SqlField(BaseModel):
    name: str
    type: Optional[str] = None
    # TODO: add more properties


class AbstractSqlBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: Optional[str] = None

    def to_sql(self, ctx: "SqlGenContext" = None) -> str:
        raise NotImplementedError

    def sql_target(self, ctx: "SqlGenContext" = None) -> str:
        ctx = ctx or use_sql_context()
        return ctx.get_template("subquery.j2").render(this=self, ctx=ctx)

    def get_fields(self) -> List[SqlField]:
        raise NotImplementedError

    def get_field_names(self) -> List[str]:
        return [f.name for f in self.get_fields()]


class AbstractSqlFunction(AbstractSqlBlock):
    input_block: Optional[AbstractSqlBlock] = None

    def __call__(self, input_block: AbstractSqlBlock) -> "AbstractSqlBlock":
        assert self.input_block is None, "input_block is already set"
        return self.model_copy(update={"input_block": input_block})

    # pipe operator
    def __or__(self, other: "AbstractSqlBlock") -> "AbstractSqlBlock":
        return other(input_block=self)


class PredefinedTemplateSqlBlock(AbstractSqlFunction):
    template_name: ClassVar[str]

    def to_sql(self, ctx: "SqlGenContext" = None) -> str:
        ctx = ctx or use_sql_context()
        params = {"this": self, "quote": lambda iden: ctx.quote(iden)}
        params.update(dict(self))
        for name, _ in self.model_computed_fields.items():
            params[name] = getattr(self, name)
        template = ctx.get_template(self.template_name)
        return ctx.render_template(template, **params)


class TemplateSqlBlock(PredefinedTemplateSqlBlock):
    template_name: str
    params: Dict[str, Any] = Field(default_factory=dict)
