import sys
from pathlib import Path
from typing import Optional

import typer
import ujson
from pydantic import ValidationError
from rich.console import Console

from ..async_typer import AsyncTyper
from ..ctl.client import initialize_client, initialize_client_sync
from ..ctl.exceptions import QueryNotFoundError
from ..ctl.utils import catch_exception, find_graphql_query, parse_cli_vars
from ..exceptions import GraphQLError
from ..utils import get_branch, write_to_file
from ..yaml import SchemaFile
from .parameters import CONFIG_PARAM
from .utils import load_yamlfile_from_disk_and_exit

app = AsyncTyper()
console = Console()


@app.callback()
def callback() -> None:
    """
    Helper to validate the format of various files.
    """


@app.command(name="schema")
@catch_exception(console=console)
async def validate_schema(schema: Path, _: str = CONFIG_PARAM) -> None:
    """Validate the format of a schema file either in JSON or YAML"""

    schema_data = load_yamlfile_from_disk_and_exit(paths=[schema], file_type=SchemaFile, console=console)
    if not schema_data:
        console.print(f"[red]Unable to find {schema}")
        raise typer.Exit(1)

    client = initialize_client()

    try:
        client.schema.validate(schema_data[0].payload)
    except ValidationError as exc:
        console.print(f"[red]Schema not valid, found {len(exc.errors())} error(s)")
        for error in exc.errors():
            loc_str = [str(item) for item in error["loc"]]
            console.print(f"  '{'/'.join(loc_str)}' | {error['msg']} ({error['type']})")
        raise typer.Exit(1)

    console.print("[green]Schema is valid !!")


@app.command(name="graphql-query")
@catch_exception(console=console)
def validate_graphql(
    query: str,
    variables: Optional[list[str]] = typer.Argument(
        None, help="Variables to pass along with the query. Format key=value key=value."
    ),
    debug: bool = typer.Option(False, help="Display more troubleshooting information."),
    branch: str = typer.Option(None, help="Branch on which to validate the GraphQL Query."),
    _: str = CONFIG_PARAM,
    out: str = typer.Option(None, help="Path to a file to save the result."),
) -> None:
    """Validate the format of a GraphQL Query stored locally by executing it on a remote GraphQL endpoint"""

    branch = get_branch(branch)

    try:
        query_str = find_graphql_query(query)
    except QueryNotFoundError:
        console.print(f"[red]Unable to find the GraphQL Query : {query}")
        sys.exit(1)

    console.print(f"[purple]Query '{query}' will be validated on branch '{branch}'.")

    variables_dict = parse_cli_vars(variables)

    client = initialize_client_sync()
    try:
        response = client.execute_graphql(
            query=query_str,
            branch_name=branch,
            variables=variables_dict,
            raise_for_error=False,
        )
    except GraphQLError as exc:
        console.print(f"[red]{len(exc.errors)} error(s) occurred while executing the query")
        for error in exc.errors:
            if isinstance(error, dict) and "message" in error and "locations" in error:
                console.print(f"[yellow] - Message: {error['message']}")
                console.print(f"[yellow]   Location: {error['locations']}")
            elif isinstance(error, str) and "Branch:" in error:
                console.print(f"[yellow] - {error}")
                console.print("[yellow]   you can specify a different branch with --branch")
        sys.exit(1)

    console.print("[green] Query executed successfully.")

    if debug:
        console.print("-" * 40)
        console.print(f"Response for GraphQL Query {query}")
        console.print(response)
        console.print("-" * 40)

    if out:
        json_string = ujson.dumps(response, indent=2, sort_keys=True)
        write_to_file(Path(out), json_string)
