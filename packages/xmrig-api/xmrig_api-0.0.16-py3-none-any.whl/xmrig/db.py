"""
XMRig Database module.

This module provides the XMRigDatabase class for database operations related to the XMRig miner.
It includes functionalities for:

- Initializing the database engine.
- Inserting data into the database.
- Retrieving data from the database.
- Deleting all miner-related data from the database.
"""

from sqlalchemy import create_engine, text, inspect
from sqlalchemy.engine import Engine
from xmrig.helpers import log, XMRigDatabaseError
from datetime import datetime
from typing import Dict, Any, Union, List
import pandas as pd
import json

class XMRigDatabase:
    """
    A class for handling database operations related to the XMRig miner.

    Attributes:
        _engines (Dict[str, Engine]): A dictionary to store database engines.
    """

    _engines = {}

    @classmethod
    def init_db(cls, db_url: str) -> Engine:
        """
        Initializes the database engine, if it already exists, it returns the existing engine.

        Args:
            db_url (str): Database URL for creating the engine.

        Returns:
            Engine: SQLAlchemy engine instance.
        """
        try:
            if db_url not in cls._engines:
                cls._engines[db_url] = create_engine(db_url)
            return cls._engines[db_url]
        except Exception as e:
            raise XMRigDatabaseError(f"An error occurred initializing the database: {e}") from e
    
    # TODO: Implement across the codebase
    @classmethod
    def get_db(cls, db_url: str) -> Engine:
        """
        Returns the database engine for the specified database URL.

        Args:
            db_url (str): Database URL for creating the engine.

        Returns:
            Engine: SQLAlchemy engine instance.
        """
        try:
            return cls._engines[db_url]
        except KeyError:
            raise XMRigDatabaseError(f"Database engine for '{db_url}' does not exist. Please initialize the database first.") from None

    @classmethod
    def check_table_exists(cls, db_url: str, table_name: str) -> bool:
        """
        Checks if the table exists in the database.

        Args:
            db_url (str): Database URL for creating the engine.
            table_name (str): Name of the table to check.

        Returns:
            bool: True if the table exists, False otherwise.
        """
        try:
            # Create an engine
            engine = cls.init_db(db_url)
            # Create an inspector
            inspector = inspect(engine)
            # Check if the table exists
            for i in inspector.get_table_names():
                if table_name[1:-1] in i:       # Remove the quotes from the table name
                    return True
            return False
        except Exception as e:
            raise XMRigDatabaseError(f"An error occurred checking if the table exists: {e}") from e
    
    @classmethod
    def insert_data_to_db(cls, json_data: Dict[str, Any], table_name: str, db_url: str) -> None:
        """
        Inserts JSON data into the specified database table.

        Args:
            json_data (Dict[str, Any]): JSON data to insert.
            table_name (str): Name of the table to insert data into.
            db_url (str): Database URL for creating the engine.
        """
        try:
            # Create a dataframe with the required columns and data
            data = {
                "timestamp": [datetime.now()],
                "full_json": [json.dumps(json_data)]
            }
            engine = cls.init_db(db_url)
            df = pd.DataFrame(data)
            # Insert data into the database
            df.to_sql(table_name, engine, if_exists="append", index=False)
            log.debug("Data inserted successfully")
        except Exception as e:
            raise XMRigDatabaseError(f"An error occurred inserting data to the database: {e}") from e
    
    @classmethod
    def fallback_to_db(cls, table_name: Union[str, List[str]], keys: List[Union[str, int]], db_url: str) -> Any:
        """
        Retrieves the data from the database using the provided table name.

        Args:
            table_name (Union[str, List[str]]): The name of the table or list of table names to use to retrieve the data.
            keys (List[Union[str, int]]): The keys to use to retrieve the data.
            db_url (str): The Database URL for creating the engine.

        Returns:
            Any: The retrieved data, or "N/A" if not available.
        """
        column_name = "full_json"
        engine = cls.init_db(db_url)
        try:
            with engine.connect() as connection:
                # special handling for backends property, enables support for xmrig-mo fork
                if len(keys) < 1 and "backend" in table_name:
                    # get all backend tables and construct the response
                    backends = []
                    miner_name = table_name.split("-")[0].lstrip("'")
                    # Connect to the database and fetch the data in column_name from the table_name for each backend
                    if cls.check_table_exists(db_url, f"{miner_name}-cpu-backend"):
                        backends.append(json.loads(connection.execute(text(f"SELECT {column_name} FROM '{miner_name}-cpu-backend' ORDER BY timestamp DESC LIMIT 1")).fetchone()[0]))
                    if cls.check_table_exists(db_url, f"{miner_name}-opencl-backend"):
                        backends.append(json.loads(connection.execute(text(f"SELECT {column_name} FROM '{miner_name}-opencl-backend' ORDER BY timestamp DESC LIMIT 1")).fetchone()[0]))
                    if cls.check_table_exists(db_url, f"{miner_name}-cuda-backend"):
                        backends.append(json.loads(connection.execute(text(f"SELECT {column_name} FROM '{miner_name}-cuda-backend' ORDER BY timestamp DESC LIMIT 1")).fetchone()[0]))
                    return backends
                # default handling
                else:
                    # Connect to the database and fetch the data in column_name from the table_name
                    result = connection.execute(text(f"SELECT {column_name} FROM {table_name} ORDER BY timestamp DESC LIMIT 1"))
                    # Fetch the last item from the result
                    data = result.fetchone()
                    if data:
                        data = json.loads(data[0])
                    # if the first key is an int then that means we are dealing with the properties that require the
                    # backends tables, remove the first item from the keys list because the backends are stored in 
                    # individual tables
                    if isinstance(keys[0], int):
                        keys.pop(0)
                    # Use the list of keys/indices to access the correct data
                    if len(keys) > 0:
                        for key in keys:
                            data = data[key]
                    return data
            return "N/A"
        except Exception as e:
            raise XMRigDatabaseError(f"An error occurred retrieving data from the database: {e}") from e
        finally:
            connection.close()

    # TODO: Check this works after recent changes
    @classmethod
    def delete_all_miner_data_from_db(cls, miner_name: str, db_url: str) -> None:
        """
        Deletes all tables related to a specific miner from the database.

        Args:
            miner_name (str): The unique name of the miner.
            db_url (str): Database URL for creating the engine.
        """
        try:
            # Use quotes to avoid SQL syntax errors
            backends_tables = [f"'{miner_name}-cpu-backend'", f"'{miner_name}-opencl-backend'", f"'{miner_name}-cuda-backend'"]
            config_table = f"'{miner_name}-config'"
            summary_table = f"'{miner_name}-summary'"
            engine = cls.init_db(db_url)
            with engine.connect() as connection:
                # Wrap the raw SQL strings in SQLAlchemy's `text` function so it isn't a raw string
                connection.execute(text(f"DROP TABLE IF EXISTS {backends_tables[0]}"))
                connection.execute(text(f"DROP TABLE IF EXISTS {backends_tables[1]}"))
                connection.execute(text(f"DROP TABLE IF EXISTS {backends_tables[2]}"))
                connection.execute(text(f"DROP TABLE IF EXISTS {config_table}"))
                connection.execute(text(f"DROP TABLE IF EXISTS {summary_table}"))
            log.debug(f"All tables for '{miner_name}' have been deleted from the database")
        except Exception as e:
            raise XMRigDatabaseError(f"An error occurred deleting miner '{miner_name}' from the database: {e}") from e

# Define the public interface of the module
__all__ = ["XMRigDatabase"]