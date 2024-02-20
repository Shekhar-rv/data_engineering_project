import container

if __name__ == "__main__":
    print("Hello, World!")
    pg_connection = container.get_pg_connection("postgres://postgres:dev@172.17.0.1:5432/postgres?schema=public")
    print("Connection established!")

    with self.pg_connection.cursor() as cursor:
        cursor.execute(
            self.query_reader.get_shop_data_query,
            {"shop_id": shop_id}
        )