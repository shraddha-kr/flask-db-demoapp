# importing the driver/connector for postgres conn
import psycopg2


class UseDatabase:

    def __init__(self, config:str) -> None:
        self.configuration = config


    def __enter__(self) -> 'cursor':
        self.conn =  psycopg2.connect(self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor


    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
