import typer
from resource_generator.cli_factory import __create_file

app = typer.Typer(no_args_is_help=True)

@app.command()
def make_model(name: str):
    """Create file model"""
    template = f"""from app.models.base_model import IDModel, TimestampModel
from pydantic import BaseModel


class {name.capitalize()}Base(BaseModel):
    pass
    # Add your field for table here

class {name.capitalize()}Model({name.capitalize()}Base, IDModel, TimestampModel, table=True):
    __table__ = '{name.lower()}s'
    """

    __create_file("models", f"{name.lower()}", "_model.py", template)
