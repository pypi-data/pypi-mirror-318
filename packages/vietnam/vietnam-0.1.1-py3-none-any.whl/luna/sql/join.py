from typing import Any, ClassVar, List, Optional

from pydantic import BaseModel, computed_field

from luna.sql.base import AbstractSqlBlock, PredefinedTemplateSqlBlock, SqlField


class JoinTarget(BaseModel):
    target: AbstractSqlBlock
    condition: str
    alias: Optional[str] = None

    # @computed_field()
    # def effective_alias(self) -> str:
    #     r = self.alias or self.target.name
    #     assert r
    #     return r


class JoinBlock(PredefinedTemplateSqlBlock):
    template_name: ClassVar[str] = "join.j2"

    base: AbstractSqlBlock
    joins: List[JoinTarget]

    def get_fields(self) -> List[SqlField]:
        fields = []
        for f in self.base.get_fields():
            fields.append(f.name)
        for block in [j.target for j in self.joins]:
            alias = block.name
            assert alias
            for f in block.get_fields():
                fields.append(f"{alias}.{f.name}")
        return [SqlField(name=f) for f in fields]

    @computed_field()
    def select_expressions(self) -> List[Any]:
        selects = []
        for fname in self.base.get_field_names():
            alias = self.base.name
            select = [f"{alias}.{fname}", f"{fname}"]
            selects.append(select)
        for block in [j.target for j in self.joins]:
            alias = block.name
            assert alias
            for fname in block.get_field_names():
                select = [f"{alias}.{fname}", f"{alias}.{fname}"]
                selects.append(select)
        return selects
