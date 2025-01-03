import typer
from resource_generator.cli_factory import __create_file
app = typer.Typer(no_args_is_help=True)

@app.command()
def make_service(name: str):
    """Create a new service file."""
    template = f"""import uuid


from app.core.base_response import AppResponseAsList, AppResponse
from app.core.filter_params import FilterParams
from app.exceptions.base_exception import AppExceptionHandler
from app.schemas.person_schema import {name.capitalize()}Request, {name.capitalize()}Response, {name.capitalize()}Update
from app.repository import {name.capitalize()}RepositoryDep


class {name.capitalize()}Service:
    def __init__(
        self,
        person_repo: {name.capitalize()}RepositoryDep
    ):
        self.person_repo = person_repo

    async def create(self, body: {name.capitalize()}Request) -> AppResponse[{name.capitalize()}Response]:
        try:
            response = self.person_repo.create(obj_in=body)
            return AppResponse(
                data=response,
                message="Create successful"
            )
        except AppExceptionHandler as e:
            raise RuntimeError(f"Error while creating: {{e}}")

    async def list(self, filter_params: FilterParams) -> AppResponseAsList[{name.capitalize()}Response]:
        try:
            response = self.person_repo.list(filter_params=filter_params)
            return AppResponseAsList(data=response)
        except AppExceptionHandler as e:
            raise f"Error while get as list {{e}}"

    async def update(self, person_id: uuid.UUID,  body: {name.capitalize()}Update):
        try:
            person_obj = self.person_repo.get_by_id(person_id)
            response = self.person_repo.update(db_obj=person_obj, obj_in=body)
            return AppResponse(data=response, message="Update success")
        except AppExceptionHandler as e:
            raise f"Error while update {{e}}"

    async def delete(self, recode_id):
        try:
            response = self.person_repo.remove(_id=recode_id)
            return AppResponse(data=response, message="Delete success")
        except AppExceptionHandler as e:
            raise f"Error while delete {{e}}"
    """

    __create_file("services", f"{name.lower()}", "_service.py", template)

