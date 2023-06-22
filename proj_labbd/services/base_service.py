from ..database import DatabaseConnection
from functools import wraps

def with_transaction_db_connection(func):
    '''Decorator to execute a function with a database connection and a transaction.'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        db_connection = DatabaseConnection()
        cursor = db_connection.cursor()

        try:
            result = func(cursor, *args, **kwargs)
            db_connection.commit()
            return result
        except Exception as e:
            db_connection.rollback()
            raise e
        finally:
            cursor.close()

    return wrapper


def with_db_connection(func):
    '''Decorator to execute a function with a database connection.'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        db_connection = DatabaseConnection()
        cursor = db_connection.cursor()

        try:
            result = func(cursor, *args, **kwargs)
            return result
        except Exception as e:
            raise e
        finally:
            cursor.close()

    return wrapper

