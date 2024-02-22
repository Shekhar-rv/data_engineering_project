class QueryFileReader:
    """
    The SQL queries found in the 'load' directory are read and stored as variables once the '__init__.py' module has been initiallised.
    The query string is (python) formatted with the Postgres connection details received from the POSTGRES_URI environment variable
    where applicable (mainly the populate_table_*.sql files).
    """
    def __init__(self) -> None:

        # Postgres create
        with open("src/sql_queries/create_shop_data.sql", "r") as f:
            self.create_shop_data_query = f.read()

# /de_project/src/sql_queries/create_shop_data.sql