import contextlib
import os
from snowflake.snowpark import Session
from snowflake.connector.connection import SnowflakeConnection
from .snowcli.cli.app.snow_connector import connect_to_snowflake as snowcli_connect_to_snowflake

@contextlib.contextmanager
def cd_temporarily(new_path):
    original_path = os.getcwd()
    os.chdir(new_path)
    try:
        yield
    finally:
        os.chdir(original_path)

def get_snowflake_connection(connection_name:str="dev") -> SnowflakeConnection:
    # Connect to Snowflake
    with cd_temporarily(os.path.expanduser("~")):
        return snowcli_connect_to_snowflake(connection_name=connection_name)

def get_snowpark_session(connection_name:str="dev") -> Session:
    builder = Session.builder
    builder._options["connection"] = get_snowflake_connection(connection_name)
    return builder.create()