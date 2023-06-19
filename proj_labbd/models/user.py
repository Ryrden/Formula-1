from flask_login import UserMixin, login_user
from ..services.user_service import UserService

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    @staticmethod
    def get(user_id):
        return User(user_id)

    @staticmethod
    def authenticate(username, password):
        login = UserService.login(username, password)

        if login is None:
            return None

        user_id, username, user_type, source_id = login

        user = User(login["user_id"])
        login_user(user)

        user_data = {
            "user_id": login["user_id"],
            "username": login["username"],
            "user_type": login["user_type"],
            "source_id": login["source_id"],
        }

        return user_data

    @staticmethod
    def get_user_by_id(user_id):
        return UserService.get_user_by_id(user_id)

    @staticmethod
    def insert_user(user):
        UserService.insert_user(user)

    @staticmethod
    def update_user(user):
        UserService.update_user(user)

    @staticmethod
    def delete_user(user_id):
        UserService.delete_user(user_id)
