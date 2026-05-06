from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # 密码加密
    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    # 密码校验
    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)