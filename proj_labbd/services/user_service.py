from ..database import DatabaseConnection as database

class UserService:
    @staticmethod
    def login(username, password):
        db_connection = database()
        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM Users U WHERE login = %s AND password = md5(%s)", (username, password))
        row = cursor.fetchone()

        if row is None:
            return None

        user_id, username, _, user_type, source_id = row

        user = {
            "user_id": user_id,
            "username": username,
            "user_type": user_type,
            "source_id": source_id
        }

        return user

    @staticmethod
    def get_user_by_id():
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM Users U WHERE U.userid = %s", (user_id,))
        row = cursor.fetchone()

        if row is None:
            return None

        user_id, username, _, user_type, source_id = row

        user = UserDAO(user_id, username, user_type, source_id)

        return user


    @staticmethod
    def get_all_users():
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()

        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        users = []

        for row in rows:
            user_id, username, _, user_type, source_id = row

            user = {
                "user_id": user_id,
                "username": username,
                "user_type": user_type,
                "source_id": source_id
            }

            users.append(user)

        return users


    @staticmethod
    def insert_user(user):
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()

        cursor.execute("INSERT INTO Users (login, password, user_type, source_id) VALUES (%s, md5(%s), %s, %s)", (user["username"], user["password"], user["user_type"], user["source_id"]))
        db_connection.commit()

        cursor.close()
        db_connection.close()


    @staticmethod
    def update_user(user):
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()

        cursor.execute("UPDATE Users SET login = %s, password = md5(%s), user_type = %s, source_id = %s WHERE userid = %s", (user["username"], user["password"], user["user_type"], user["source_id"], user["user_id"]))

        db_connection.commit()

        cursor.close()
        db_connection.close()


    @staticmethod
    def delete_user(user_id):
        db_connection = database.DatabaseConnection()
        cursor = db_connection.cursor()

        cursor.execute("DELETE FROM Users WHERE userid = %s", (user_id,))

        db_connection.commit()

        cursor.close()
        db_connection.close()
        