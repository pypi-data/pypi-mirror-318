import psycopg2
from psycopg2 import sql
from psplpy.other_utils import get_env
from .enums import DbBackend


def create_db(db_backend: str = DbBackend.POSTGRESQL):
    if db_backend == DbBackend.POSTGRESQL:
        conn = psycopg2.connect(
            dbname="postgres",
            user=get_env('DB_USER'),
            password=get_env('DB_PASSWORD'),
            host=get_env('DB_HOST'),
            port=get_env('DB_PORT'),
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(get_env('DB_NAME'))))
        cur.close()
        conn.close()
    else:
        raise ValueError(f'Database type {db_backend} not supported')
