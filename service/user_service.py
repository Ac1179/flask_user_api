from flask_jwt_extended import create_access_token
from dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def register(self, username, password):
        if not username or not password:
            return {"code": 400, "msg": "用户名或密码不能为空"}

        if self.user_dao.get_by_username(username):
            return {"code": 409, "msg": "用户名已存在"}

        try:
            user = self.user_dao.create_user(username, password)
            return {"code": 200, "msg": "注册成功", "data": user.to_dict()}
        except Exception as e:
            return {"code": 500, "msg": f"注册失败：{str(e)}"}

    def login(self, username, password):
        user = self.user_dao.get_by_username(username)
        if not user:
            return {"code": 404, "msg": "用户不存在"}

        if not user.check_password(password):
            return {"code": 401, "msg": "密码错误"}

        token = create_access_token(identity=user.id)
        return {
            "code": 200,
            "msg": "登录成功",
            "data": {
                "token": token,
                "user": user.to_dict()
            }
        }