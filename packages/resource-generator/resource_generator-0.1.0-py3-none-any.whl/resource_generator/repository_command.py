from pathlib import Path

import typer
from rich.console import Console
from resource_generator.cli_factory import __create_file, BASE_DIR, __format


app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command()
def make_repository(name: str):
    """Create a new repository file."""
    template = f"""from typing import Annotated

from app.core.database.context import get_db
from app.models.{name.lower()}_model import {name.capitalize()}Model
from app.schemas.{name.lower()}_schema import {name.capitalize()}Request, {name.capitalize()}Update
from app.repository.base_repo import BaseRepo
from fastapi import Depends
from sqlmodel import Session

class {name.capitalize()}Repository(BaseRepo[{name.capitalize()}Model, {name.capitalize()}Request, {name.capitalize()}Update]):
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        super().__init__({name.capitalize()}Model, db)
    """

    created = __create_file("repository", f"{name.lower()}", "_repository.py", template)
    if created:
        content = f"""from app.repository.{name.lower()}_repository import {name.capitalize()}Repository

{name.capitalize()}RepositoryDep = Annotated[{name.capitalize()}Repository, Depends({name.capitalize()}Repository)]
        """

        repository_initializer = Path(f"{BASE_DIR}/repository/__init__.py")
        if repository_initializer.exists():
            with repository_initializer.open('a') as file:
                file.write(content)

            __format(file_path=repository_initializer)
        else:
            print(f"{repository_initializer} does not exist!")