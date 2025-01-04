from functools import cached_property
from typing import ClassVar, List, Optional

from pydantic import Field, model_validator

from .base import AbstractSqlBlock, AbstractSqlFunction, PredefinedTemplateSqlBlock, SqlField
from .ctx import SqlGenContext


class SqlQuery(AbstractSqlFunction):
    sql: str

    def to_sql(self, ctx: SqlGenContext) -> str:
        template = ctx.jinja.from_string(self.sql)
        return ctx.render_template(template)


class SqlTarget(AbstractSqlBlock):
    target: str
    fields: List[SqlField] = Field(default_factory=list)

    def to_sql(self, ctx: SqlGenContext) -> str:
        return "select * from " + self.sql_target(ctx)

    def sql_target(self, ctx: SqlGenContext) -> str:
        return self.target

    def get_fields(self):
        return self.fields


class SelectBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "select.j2"

    selects: Optional[List[str]] = None
    filters: Optional[List[str]] = None


class TableDiff(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "table_diff.j2"

    source: AbstractSqlBlock
    target: AbstractSqlBlock
    key_columns: List[str]


class CteBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "cte.j2"

    blocks: List[AbstractSqlBlock]


class StackBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "stack.j2"

    blocks: List[AbstractSqlBlock]

    # validate that the blocks are all stackable
    @model_validator(mode="after")
    def validate_blocks(self):
        names = [e.name for e in self.blocks if e.name]
        assert len(names) == len(set(names)), "Blocks must have unique names."
        for block in self.blocks[1:]:
            if not isinstance(block, AbstractSqlFunction):
                raise ValueError(f"Block {block} is not stackable")
        return self

    @cached_property
    def cloned_blocks(self):
        cloned = [block.model_copy() for block in self.blocks]
        for idx, block in enumerate(cloned):
            block.name = block.name or f"block_{idx}"
        return cloned

    def to_sql(self, ctx):
        if len(self.blocks) == 1:
            return self.blocks[0].to_sql(ctx)
        else:
            # do a copy of the blocks since we might assign names to them
            for idx, block in enumerate(self.cloned_blocks):
                if idx == 0:
                    continue
                else:
                    last_block = self.cloned_blocks[idx - 1]
                    target_block = SqlTarget(target=last_block.name)
                    self.cloned_blocks[idx] = block(target_block)
            return super().to_sql(ctx)


class UnionAll(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "union_all.j2"

    blocks: List[AbstractSqlBlock]


class HashData(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "hash_data.j2"
