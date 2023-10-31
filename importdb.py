from sqlalchemy import create_engine #conexion a BBDD
from sqlalchemy import text #transforma un texto a una query
import pandas as pd
import os

POSTGRES_PROTOCOL = os.environ.get("DB_PROTOCOL", "postgresql")
POSTGRES_HOST = os.environ.get("DB_HOST", "localhost")
POSTGRES_PORT = os.environ.get("DB_PORT", "5432")
POSTGRES_BBDD = os.environ.get("DB_NAME", "challenge_rocking")
POSTGRES_USER = os.environ.get("DB_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("DB_PASSWORD", "kpojoa2010")


database_config = {
    'host': POSTGRES_HOST,
    'dbname': POSTGRES_BBDD,
    'user': POSTGRES_USER,
    'password': POSTGRES_PASSWORD,
    'port': POSTGRES_PORT,
    'protocol': POSTGRES_PROTOCOL,
}

print(f'Database connection: {database_config}')

class PostgreSQLConnection:

    STR_CONN=f'{POSTGRES_PROTOCOL}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_BBDD}'
    engine = None

    def __init__(self):
        self.engine = create_engine(self.STR_CONN)


    def save_data_to_postgres(self, table_name: str, data: pd.DataFrame):

        data.to_sql(table_name, self.engine, if_exists='append', index=False)
        print(table_name+" created")