import psycopg2
import os
from dotenv import dotenv_values

env = dotenv_values(os.path.join(os.path.dirname(__file__), ".env"))

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Singleton Database Connection"""
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = psycopg2.connect(
                host=env["DB_HOST"],
                port=env["DB_PORT"],
                user=env["DB_USER"],
                password=env["DB_PASSWORD"],
                database=env["DB_DATABASE"],
            )
            cls._instance.autocommit = False
        return cls._instance
