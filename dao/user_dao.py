from dao.base_dao import BaseDAO
from models.user_model import User

class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__(User)

    def get_by_username(self, username):
        return self.get_by_field(username=username)

    def create_user(self, username, password):
        user = User(username=username)
        user.set_password(password)
        return self.add(user)