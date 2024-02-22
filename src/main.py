import container
from os import environ
from query_file_reader import QueryFileReader


POSTGRES_URI = environ.get("POSTGRES_URI")

if __name__ == "__main__":
    pg_connection = container.get_pg_connection(postgres_uri=POSTGRES_URI)
    print("Connection established!")
    with pg_connection.cursor() as cursor:
        cursor.execute(QueryFileReader().create_shop_data_query)
    print("Table created!")
    exit()
    with self.pg_connection.cursor() as cursor:
        cursor.execute(
            self.query_reader.get_shop_data_query,
            {"shop_id": shop_id}
        )