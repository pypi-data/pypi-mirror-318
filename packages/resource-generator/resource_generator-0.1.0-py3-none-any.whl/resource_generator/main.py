import typer

app = typer.Typer(name="khunratana-commander")


from resource_generator.model_command import app as model_app
from resource_generator.controller_command import app as controller_app
from resource_generator.repository_command import app as repository_app
from resource_generator.schema_command import app as schema_app
from resource_generator.service_command import app as service_app

app.add_typer(model_app, name="model")
app.add_typer(controller_app, name="controller")
app.add_typer(repository_app, name="repository")
app.add_typer(schema_app, name="schema")
app.add_typer(service_app, name="service")


@app.callback()
def callback():
    """
    Resource generator
    """

    