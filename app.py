from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import config

# 初始化扩展
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # 绑定扩展
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝图（你原版接口）
    from api.user_api import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/user')

    # 健康检查
    @app.route('/')
    def index():
        return {"code": 200, "msg": "Flask 线上部署版运行正常"}

    return app

# 本地测试用
