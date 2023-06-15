import psycopg2

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = psycopg2.connect(
                host="localhost",
                port="5432",
                user="postgres",
                password="123456",
                database="postgres"
            )
        return cls._instance