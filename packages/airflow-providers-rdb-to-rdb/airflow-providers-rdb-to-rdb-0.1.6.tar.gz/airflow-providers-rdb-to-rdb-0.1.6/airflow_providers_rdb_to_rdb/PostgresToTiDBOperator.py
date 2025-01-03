from typing import Any, Dict, List, Optional

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class SQLOperations:
    def __init__(self, source_table: str, target_table: str, target_db_code: str):
        """
        Initialize SQLOperations with table information
        """
        # Initialize paths and imports
        import sys

        sys.path.append("/app/mount/")
        from utils.migration import pg_to_tidb

        self.pg_to_tidb = pg_to_tidb
        self.source_table = source_table
        self.target_table = target_table
        self.target_db_code = target_db_code

    def create_table(
        self,
        source_conn,
        exclude_columns: Optional[List[str]] = None,
        column_schemas: Optional[Dict] = None,
        include_columns: Optional[List[Dict]] = None,
        include_primary_key: bool = True,
    ) -> str:
        """
        Create target table if not exists
        """
        return self.pg_to_tidb.create_table_statement(
            self.source_table,
            self.target_table,
            source_conn,
            exclude_columns=exclude_columns,
            column_schemas=column_schemas,
            include_columns=include_columns,
            include_primary_key=include_primary_key,
        )

    def create_indices(self) -> List[str]:
        """Create index SQL statements for time-related columns."""

        def generate_index_name(column: str) -> str:
            base_name = f"idx_{self.target_table}_{column}"
            return base_name if len(base_name) <= 64 else f"idx_ods_{self.target_table}_{column}"

        return [
            f"""
            CREATE INDEX IF NOT EXISTS {generate_index_name(column)}
            ON {self.target_db_code}.{self.target_table} ({column});
            """
            for column in ["updated_at", "table_updated_time"]
        ]

    def get_latest_update_time_sql(self, updated_column: str = "updated_at") -> str:
        """Generate SQL to get the latest update time"""
        return f"""
            SELECT DATE_FORMAT(max({updated_column}), '%Y-%m-%d %H:%i:%S') as updated_at
            FROM {self.target_table}
        """

    def get_columns_list_sql(self) -> str:
        """Generate SQL to get column list"""
        return f"""
            SELECT DISTINCT column_name
            FROM information_schema.columns
            WHERE table_name = '{self.source_table}'
        """

    def process_columns_list(
        self,
        columns_query: List[Any],
        exclude_columns: Optional[List[str]] = None,
        include_columns: Optional[List[Dict]] = None,
    ) -> str:
        """
        Process the columns list by excluding specified columns and including custom columns.
        """
        columns = set(column[0] for column in columns_query)
        exclude_set = set(exclude_columns or [])

        # Filter out excluded columns
        filtered_columns = [col for col in columns if col not in exclude_set]

        # Add custom columns
        custom_columns = [
            f"'{col['column_value']}' AS {col['column_name']}"
            for col in (include_columns or [])
            if col["column_name"] not in exclude_set
        ]
        return ", ".join(filtered_columns + custom_columns)

    def generate_migration_sql(
        self,
        columns_list: str,
        latest_update_time: Optional[str] = None,
        updated_column: str = "updated_at",
        force_initialization: bool = False,
    ) -> str:
        """
        Generate SQL for data migration based on specified conditions.
        """
        base_query = f"SELECT {columns_list} FROM {self.source_table}"

        if force_initialization:
            print("Forcing initialization")
            return base_query

        if latest_update_time:
            time_filter = f"WHERE {updated_column} >= '{latest_update_time}'::timestamp - INTERVAL '30' MINUTE"
            order_by = f"ORDER BY {updated_column} ASC"
            return f"{base_query} {time_filter} {order_by}"

        return base_query


class PostgresToTiDBOperator(BaseOperator):
    """
    Custom Airflow operator to migrate data from PostgreSQL to TiDB
    """

    @apply_defaults
    def __init__(
        self,
        server: str,
        source_db_code: str,
        source_table: str,
        target_db_code: str,
        target_table: str,
        exclude_columns: Optional[List[str]] = None,
        column_schemas: Optional[Dict] = None,
        include_columns: Optional[List[Dict]] = None,
        include_primary_key: bool = True,
        updated_column: str = "updated_at",
        force_initialization: bool = False,
        batch_size: int = 10000,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        self.source_db_code = source_db_code
        self.source_table = source_table
        self.target_db_code = target_db_code
        self.target_table = target_table
        self.exclude_columns = exclude_columns or []
        self.column_schemas = column_schemas or {}
        self.include_columns = include_columns or []
        self.include_primary_key = include_primary_key
        self.updated_column = updated_column
        self.force_initialization = force_initialization
        self.batch_size = batch_size

    def execute(self, context: Dict) -> None:
        """Execute the migration from PostgreSQL to TiDB"""
        import sys

        sys.path.append("/app/mount/")

        from utils import mysql_functions, postgres_functions
        from utils.get_connection import GetConnection
        from utils.migration import pg_to_tidb

        # Initialize SQL operations
        sql_ops = SQLOperations(
            source_table=self.source_table, target_table=self.target_table, target_db_code=self.target_db_code
        )

        # Initialize connections
        source_conn_obj = GetConnection(self.server)
        source_conn = source_conn_obj.get_pg_connection(self.source_db_code)

        conn_obj = GetConnection(self.server)
        tidb_conn = conn_obj.get_tidb_connection("datawarehouse", database=self.target_db_code)

        # Create target table
        create_statement = sql_ops.create_table(
            source_conn,
            self.exclude_columns,
            self.column_schemas,
            self.include_columns,
            self.include_primary_key,
        )
        self.log.info(f"Create statement: {create_statement}")
        mysql_functions.execute_mysql_sql(tidb_conn, create_statement)

        # Create indices
        index_statements = sql_ops.create_indices()
        self.log.info(f"Index statements: {index_statements}")
        for statement in index_statements:
            mysql_functions.execute_mysql_sql(tidb_conn, statement)

        # Get latest update time if not provided
        latest_time_sql = sql_ops.get_latest_update_time_sql(self.updated_column)
        self.log.info(f"Latest time SQL: {latest_time_sql}")
        results = mysql_functions.fetchall_from_mysql(tidb_conn, latest_time_sql)
        latest_update_time = results[0]["updated_at"]
        self.log.info(f"Latest update time: {latest_update_time}")

        # Get and process columns list
        columns_sql = sql_ops.get_columns_list_sql()
        columns_query = postgres_functions.fetchall_from_postgres(source_conn, columns_sql)
        columns_list = sql_ops.process_columns_list(columns_query, self.exclude_columns, self.include_columns)
        self.log.info(f"Columns list: {columns_list}")

        # Generate and execute migration SQL
        migration_sql = sql_ops.generate_migration_sql(
            columns_list, latest_update_time, self.updated_column, self.force_initialization
        )
        self.log.info(f"Migration SQL: {migration_sql}")

        # Execute migration
        pg_to_tidb.postgres_to_tidb_by_updated_column(
            migration_sql,
            self.target_table,
            source_conn,
            tidb_conn,
            batchsize=self.batch_size,
            updated_column=self.updated_column,
        )
