import psycopg2
#from dotenv import dotenv_values

env = {
    "DB_HOST": "localhost",
    "DB_PORT": 5432,
    "DB_USER": "postgres",
    "DB_PASSWORD": "0859",
    "DB_DATABASE": "postgres"
}

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = psycopg2.connect(
                host=env["DB_HOST"] or "localhost",
                port=env["DB_PORT"] or 5432,
                user=env["DB_USER"] or "postgres",
                password=env["DB_PASSWORD"] or "postgres",
                database=env["DB_DATABASE"] or "postgres"
            )
        return cls._instance