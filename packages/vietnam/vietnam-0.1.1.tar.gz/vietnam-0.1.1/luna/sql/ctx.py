from functools import cache
from pathlib import Path
from typing import List, Optional, Tuple

import jinja2

from luna.ctx import set_context, use_factory

parent_dir = Path(__file__).parent


@cache
def create_jinja(search_paths: Tuple[Path] = None) -> jinja2.Environment:
    loader = jinja2.FileSystemLoader(searchpath=search_paths)
    jinja = jinja2.Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=loader,
        undefined=jinja2.StrictUndefined,
    )
    return jinja


class SqlGenContext:
    def __init__(self, search_paths: Optional[List[Path]] = None):
        if search_paths is None:
            search_paths = []
        search_paths.append(parent_dir / "templates")
        self._params = {}
        self.jinja = create_jinja(tuple(search_paths))

    def get_template(self, name: str) -> jinja2.Template:
        return self.jinja.get_template(name)

    def render_template(self, template: jinja2.Template | str, **kwargs) -> str:
        if isinstance(template, str):
            template = self.get_template(template)
        extra_params = {**self.params, "ctx": self}
        return template.render(**kwargs, **extra_params)

    @property
    def params(self):
        """Extra params for rendering templates."""
        return self._params

    def quote(self, identifier: str) -> str:
        # postgresql
        return f'"{identifier}"'


# re-export for type hinting
use_sql_context = use_factory(SqlGenContext, "sql")


def set_sql_context(ctx: SqlGenContext):
    return set_context(sql=ctx)


ExecutionContext = SqlGenContext
