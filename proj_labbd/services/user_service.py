from ..database import DatabaseConnection as database
from .base_service import with_db_connection

class UserService:
    @staticmethod
    def _get_dto_user(user_id, username, user_type, source_id):
        return {
            "user_id": user_id,
            "username": username,
            "type": user_type,
            "source_id": source_id,
        }

    @staticmethod
    def login(username, password):
        db_connection = database()
        cursor = db_connection.cursor()
        
        query = ("SELECT U.userid, U.login, U.type, U.source_id FROM Users U WHERE login = %s AND password = md5(%s)")
        params = (username, password)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None
            
        return UserService._get_dto_user(*row)

    @staticmethod
    def get_user_by_id(user_id):
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()

        query = ("SELECT U.userid, U.login, U.type, U.source_id FROM Users U WHERE U.userid = %s")
        params = (user_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return UserService._get_dto_user(*row)

    @staticmethod
    def get_all_users():
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()

        query = ("SELECT U.userid, U.login, U.type, U.source_id FROM Users;")

        cursor.execute(query)
        rows = cursor.fetchall()

        users = []

        for row in rows:
            users.append(UserService._get_dto_user(*row))

        return users