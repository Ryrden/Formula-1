from flask_login import UserMixin, login_user
from ..services.user_service import UserService

class User(UserMixin):
    def __init__(self, id):
        '''Constructor for the User class'''
        self.id = id

    @staticmethod
    def get(user_id):
        '''Returns a user object based on the user_id'''
        return User(user_id)

    @staticmethod
    def authenticate(username, password):
        '''Returns a user object if the username and password are correct'''
        login = UserService.login(username, password)

        if login is None:
            return None

        user = User(login["user_id"])
        login_user(user)

        return login

    @staticmethod
    def get_user_by_id(user_id):
        '''Returns a user object based on the user_id'''
        return UserService.get_user_by_id(user_id)

    @staticmethod
    def insert_user(user):
        '''Inserts a user object into the database'''
        UserService.insert_user(user)

    @staticmethod
    def update_user(user):
        '''Updates a user object in the database'''
        UserService.update_user(user)

    @staticmethod
    def delete_user(user_id):
        '''Deletes a user object from the database'''
        UserService.delete_user(user_id)
