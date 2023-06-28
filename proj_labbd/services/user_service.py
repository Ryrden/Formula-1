from .base_service import with_db_connection
from .base_service import with_transaction_db_connection


class UserService:
    @staticmethod
    def _get_dto_user(user_id, username, user_type, source_id):
        """Returns a dictionary with the user data"""
        return {
            "user_id": user_id,
            "username": username,
            "name": UserService.get_name(user_type, source_id),
            "type": user_type,
            "source_id": source_id,
        }

    @staticmethod
    @with_db_connection
    def login(cursor, username, password):
        """Returns a dictionary with the user data if the user exists, None otherwise"""
        query = "SELECT U.userid, U.login, U.type, U.source_id FROM Users U WHERE login = %s AND password = md5(%s)"
        params = (username, password)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        UserService.register_log(row[0])

        return UserService._get_dto_user(*row)

    @staticmethod
    @with_transaction_db_connection
    def register_log(cursor, user_id):
        """Registers a log in the database"""
        query = "INSERT INTO log_table (userid) VALUES (%s)"
        params = (user_id,)

        cursor.execute(query, params)

    @staticmethod
    @with_db_connection
    def get_user_by_id(cursor, user_id):
        query = "SELECT U.userid, U.login, U.type, U.source_id FROM Users U WHERE U.userid = %s"
        params = (user_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return UserService._get_dto_user(*row)

    @staticmethod
    @with_db_connection
    def get_name(cursor, user_type, source_id):
        """Returns the name of the user"""
        params = (str(source_id),)

        match user_type:
            case "DRIVER":
                query = "SELECT CONCAT(D.forename, ' ' , D.surname) AS name FROM Driver D WHERE D.driverid = %s"
                cursor.execute(query, params)

            case "RACING_TEAM":
                query = "SELECT C.name FROM Constructors C WHERE C.constructorid = %s"

            case "ADMIN":
                query = "SELECT U.login FROM Users U WHERE U.source_id = %s"

        cursor.execute(query, params)
        name = cursor.fetchone()[0]

        return name

    @staticmethod
    @with_db_connection
    def get_all_users(cursor):
        """Returns a list with all the users"""
        query = "SELECT U.userid, U.login, U.type, U.source_id FROM Users;"

        cursor.execute(query)
        rows = cursor.fetchall()

        users = []

        for row in rows:
            users.append(UserService._get_dto_user(*row))

        return users
