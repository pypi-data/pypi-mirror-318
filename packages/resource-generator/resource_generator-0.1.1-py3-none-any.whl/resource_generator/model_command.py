import typer
from resource_generator.cli_factory import __create_file

app = typer.Typer(no_args_is_help=True)

@app.command()
def name(model_name: str):
    """Create file model"""
    template = f"""from app.models.base_model import IDModel, TimestampModel
from pydantic import BaseModel


class {model_name.capitalize()}Base(BaseModel):
    pass
    # Add your field for table here

class {model_name.capitalize()}Model({model_name.capitalize()}Base, IDModel, TimestampModel, table=True):
    __table__ = '{model_name.lower()}s'
    """

    __create_file("models", f"{model_name.lower()}", "_model.py", template)
