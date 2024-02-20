from psycopg2 import connect
from psycopg2.extensions import connection


postgres_connection = None

def get_pg_connection(postgres_uri: str) -> connection:
    global postgres_connection
    if postgres_connection is None:
        print("Establishing connection...")
        pg_uri = postgres_uri.split("?schema")[0]
        print(pg_uri)
        postgres_connection = connect(pg_uri)
        print("Connection established!")
    return postgres_connection