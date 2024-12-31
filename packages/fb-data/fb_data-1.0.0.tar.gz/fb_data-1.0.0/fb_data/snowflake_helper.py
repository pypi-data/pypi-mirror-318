import warnings
from sqlalchemy.exc import SAWarning
warnings.filterwarnings("ignore", category=SAWarning, message=".*flatten.*")

import snowflake.connector
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from snowflake.sqlalchemy.snowdialect import SnowflakeDialect


class Snowflake:
    def __init__(self, **kwargs):
        """
        Initialize the Snowflake connector.
        Accepts dynamic connection parameters for Snowflake.
        """
        self.connection_params = kwargs
        self.connection = None
        self.cursor = None
        self.engine = None

        # Check if optional parameters are provided
        self.database = kwargs.get("database", None)
        self.schema = kwargs.get("schema", None)

        self._connect()

    def _connect(self):
        """
        Establish a connection to Snowflake.
        """
        try:
            # Snowflake Native Connector
            self.connection = snowflake.connector.connect(**self.connection_params)
            self.cursor = self.connection.cursor()
            print("Connected to Snowflake successfully!")

            # SQLAlchemy Engine for Pandas Integration
            SnowflakeDialect.supports_statement_cache = False
            self.engine = create_engine(URL(**self.connection_params))
        except Exception as e:
            raise ConnectionError(f"Error connecting to Snowflake: {e}")

    def query(self, query_string: str, output: str = "raw"):
        """
        Execute a query on Snowflake and fetch results when applicable.

        Args:
            query_string (str): The SQL query to execute.
            output (str): Output format ('pandas' or 'raw') for fetching results.

        Returns:
            pd.DataFrame or list of tuples: Query results when applicable.
            str: Snowflake's return message for queries with no results.
        """
        if not self.cursor:
            raise ConnectionError("Not connected to Snowflake. Connection may have failed during initialization.")

        try:
            self.cursor.execute(query_string)

            # If there are results to fetch
            if self.cursor.description:
                data = self.cursor.fetchall()
                columns = [col[0] for col in self.cursor.description]

                if output == "pandas":
                    return pd.DataFrame(data, columns=columns)
                elif output == "raw":
                    return data
                else:
                    raise ValueError("Invalid output format. Use 'pandas' or 'raw'.")
            else:
                # Return Snowflake's response for non-fetch queries
                return self.cursor.sfqid  # Snowflake Query ID as confirmation message
        except snowflake.connector.errors.ProgrammingError as e:
            raise RuntimeError(f"Error executing query: {e}")


    def write_pandas(self, df, table_name, if_exists):
        if not self.engine:
            raise ConnectionError("SQLAlchemy engine not initialized. Connection may have failed during initialization.")

        valid_if_exists = ['append', 'replace', 'fail']
        if if_exists not in valid_if_exists:
            raise ValueError(f"Invalid value for if_exists. Possible values are: {', '.join(valid_if_exists)}")

        try:
            df.to_sql(name=table_name, con=self.engine, if_exists=if_exists, index=False, method='multi')
            print(f"Successfully wrote {len(df)} rows to {table_name}.")
        except Exception as e:
            raise RuntimeError(f"Error writing DataFrame to Snowflake: {e}")

    def write(self, df: pd.DataFrame, table_name: str, if_exists: str = "append"):
        """
        Write a Pandas DataFrame to Snowflake.

        Args:
            df (pd.DataFrame): The DataFrame to write.
            table_name (str): The target table name in Snowflake.
            if_exists (str): Behavior if the table exists ('append', 'replace', 'fail').

        Raises:
            ValueError: If the input type or if_exists value is invalid.
            RuntimeError: If the write operation fails.
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a Pandas DataFrame.")

        if not self.engine:
            raise ConnectionError(
                "SQLAlchemy engine not initialized. Connection may have failed during initialization.")

        valid_if_exists = ["append", "replace", "fail"]
        if if_exists not in valid_if_exists:
            raise ValueError(f"Invalid value for if_exists. Possible values are: {', '.join(valid_if_exists)}")

        try:
            # Explicitly include schema in the table reference
            df.to_sql(
                name=table_name,
                con=self.engine,
                if_exists=if_exists,
                index=False,
                schema=self.schema,  # Explicit schema
                method="multi"
            )
            print(f"Successfully wrote {len(df)} rows to {self.schema}.{table_name}.")
        except Exception as e:
            raise RuntimeError(f"Error writing DataFrame to Snowflake: {e}")

    def close(self):
        """
        Close all connections to Snowflake.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if self.engine:
            self.engine.dispose()
        print("All connections to Snowflake closed.")


    def database_privileges(self, databases, roles, grants, privilege_action="GRANT", dry_run=True):
        """
        Grants or revokes privileges on multiple Snowflake databases for multiple roles.

        Args:
            databases (list[str]): List of database names.
            roles (list[str]): List of roles to grant or revoke privileges for.
            grants (list[str]): List of privileges (e.g., ["USAGE", "MONITOR"]).
            privilege_action (str): Either "GRANT" or "REVOKE". Default is "GRANT".
            dry_run (bool): If True, only print queries instead of executing. Default is True.
        """
        errors = []

        # Determine the preposition based on the privilege action
        preposition = "TO" if privilege_action.upper() == "GRANT" else "FROM"

        for database in databases:
            for role in roles:
                for grant in grants:
                    query_str = f"{privilege_action.upper()} {grant} ON DATABASE {database} {preposition} ROLE {role}"

                    if dry_run:
                        print("[DRY RUN]", query_str)
                    else:
                        try:
                            self.cursor.execute(query_str)
                        except Exception as e:
                            errors.append((query_str, str(e)))

        # Handle errors and print status
        if errors:
            print("Some database-level queries failed to execute:")
            for failed_query, err_msg in errors:
                print(f"  Query: {failed_query}")
                print(f"  Error: {err_msg}")
        else:
            print(
                "All database-level queries printed successfully (dry run)."
                if dry_run
                else "All database-level privileges processed successfully."
            )


    def schema_privileges(
        self,
        database,
        roles,
        grants,
        privilege_action="GRANT",
        schemas=None,
        include_all_schemas=False,
        include_future_schemas=False,
        dry_run=True,
    ):
        """
        Grants or revokes privileges on schema(s) within a Snowflake database for multiple roles.

        Args:
            database (str): Name of the Snowflake database.
            roles (list[str]): List of roles to grant or revoke privileges for.
            grants (list[str]): List of privileges (e.g., ["USAGE", "CREATE SCHEMA"]).
            privilege_action (str): Either "GRANT" or "REVOKE". Default is "GRANT".
            schemas (list[str]): List of schema names. Ignored if include_all_schemas=True.
            include_all_schemas (bool): If True, grants privileges on all existing schemas in the database.
            include_future_schemas (bool): If True, grants privileges on future schemas in the database.
            dry_run (bool): If True, only print queries instead of executing. Default is True.
        """
        errors = []

        # Determine the preposition based on the privilege action
        preposition = "TO" if privilege_action.upper() == "GRANT" else "FROM"

        # 1. Fetch schema names if include_all_schemas is True
        if include_all_schemas:
            try:
                self.cursor.execute(f"SHOW SCHEMAS IN DATABASE {database}")
                all_schemas = self.cursor.fetchall()
                schema_names = [row[1] for row in all_schemas]  # Typically, schema name is in the second column
            except Exception as e:
                print(f"Error fetching schemas from database {database}: {e}")
                return
        else:
            schema_names = schemas or []

        # 2. Grant or revoke privileges for each schema and role
        for schema_name in schema_names:
            for role in roles:
                for grant in grants:
                    query_str = f"{privilege_action.upper()} {grant} ON SCHEMA {database}.{schema_name} {preposition} ROLE {role}"

                    if dry_run:
                        print("[DRY RUN]", query_str)
                    else:
                        try:
                            self.cursor.execute(query_str)
                        except Exception as e:
                            errors.append((query_str, str(e)))

        # 3. Handle future schemas if requested
        if include_future_schemas:
            for role in roles:
                for grant in grants:
                    query_str_future = f"{privilege_action.upper()} {grant} ON FUTURE SCHEMAS IN DATABASE {database} {preposition} ROLE {role}"

                    if dry_run:
                        print("[DRY RUN]", query_str_future)
                    else:
                        try:
                            self.cursor.execute(query_str_future)
                        except Exception as e:
                            errors.append((query_str_future, str(e)))

        # 4. Report errors or success
        if errors:
            print("Some schema-level queries failed to execute:")
            for failed_query, err_msg in errors:
                print(f"  Query: {failed_query}")
                print(f"  Error: {err_msg}")
        else:
            print(
                "All schema-level queries printed successfully (dry run)."
                if dry_run
                else "All schema-level privileges processed successfully."
            )


    def schema_object_privileges(
        self,
        database,
        schemas,
        roles,
        objects,
        privilege_action="GRANT",
        dry_run=True,
    ):
        """
        Grants or revokes privileges for various Snowflake objects in multiple schemas.

        Args:
            database (str): Name of the database.
            schemas (list[str]): List of schema names.
            roles (list[str]): List of roles to grant or revoke privileges for.
            objects (list[dict]): List of objects and grants with structure:
                [
                    {
                        'objects': ['TABLES', 'VIEWS'],
                        'grants': ['SELECT'],
                        'include_future_objects': True
                    },
                    {
                        'objects': ['FUNCTIONS'],
                        'grants': ['USAGE'],
                        'include_future_objects': False
                    }
                ]
            privilege_action (str): Either "GRANT" or "REVOKE". Default is "GRANT".
            dry_run (bool): If True, only print queries instead of executing. Default is True.
        """
        errors = []

        # Determine the preposition based on the privilege action
        preposition = "TO" if privilege_action.upper() == "GRANT" else "FROM"

        for schema in schemas:
            for obj in objects:
                for object_type in obj["objects"]:
                    for grant in obj["grants"]:
                        # Grant or revoke on all objects
                        query_string = f"{privilege_action.upper()} {grant} ON ALL {object_type} IN SCHEMA {database}.{schema} {preposition} ROLE"

                        # Execute for each role
                        for role in roles:
                            final_query = f"{query_string} {role}"
                            if dry_run:
                                print("[DRY RUN]", final_query)
                            else:
                                try:
                                    self.cursor.execute(final_query)
                                except Exception as e:
                                    errors.append((final_query, str(e)))

                        # Grant or revoke on future objects if requested
                        if obj.get("include_future_objects", False):
                            future_query_string = f"{privilege_action.upper()} {grant} ON FUTURE {object_type} IN SCHEMA {database}.{schema} {preposition} ROLE"
                            for role in roles:
                                final_future_query = f"{future_query_string} {role}"
                                if dry_run:
                                    print("[DRY RUN]", final_future_query)
                                else:
                                    try:
                                        self.cursor.execute(final_future_query)
                                    except Exception as e:
                                        errors.append((final_future_query, str(e)))

        # Report errors or success
        if errors:
            print("Some queries failed to execute:")
            for failed_query, err_msg in errors:
                print(f"  Query: {failed_query}")
                print(f"  Error: {err_msg}")
        else:
            print(
                "All queries printed successfully (dry run)."
                if dry_run
                else "All privileges processed successfully."
            )
