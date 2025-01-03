import typer
from resource_generator.cli_factory import __create_file

app = typer.Typer(no_args_is_help=True)

@app.command()
def make_schema(name: str):
    template = f"""from typing import Optional

from app.models.{name.lower()}_model import {name.capitalize()}Base, {name.capitalize()}Model
from pydantic import BaseModel


class {name.capitalize()}Request({name.capitalize()}Base):
    pass


class {name.capitalize()}Update(BaseModel):
    pass


class {name.capitalize()}Response({name.capitalize()}Model):
    pass
    """

    __create_file("schemas", f"{name.lower()}", "_schema.py", template)
