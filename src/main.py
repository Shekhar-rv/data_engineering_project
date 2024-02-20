import container

if __name__ == "__main__":
    print("Hello, World!")
    # "postgresql://postgres:postgres@172.19.0.2:5432/data_pipeline?schema=public"
    pg_connection = container.get_pg_connection("postgresql://postgres:postgres@172.19.0.2:5432/data_pipeline?schema=public")
    print("Connection established!")
    with pg_connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS shop_data (
                id SERIAL PRIMARY KEY,
                shop_id INTEGER NOT NULL,
                shop_name VARCHAR(255) NOT NULL,
                shop_address VARCHAR(255) NOT NULL,
                shop_phone VARCHAR(255) NOT NULL,
                shop_email VARCHAR(255) NOT NULL
            );
            """
        )
    pg_connection.commit()
    print("Table created!")
    exit()
    with self.pg_connection.cursor() as cursor:
        cursor.execute(
            self.query_reader.get_shop_data_query,
            {"shop_id": shop_id}
        )