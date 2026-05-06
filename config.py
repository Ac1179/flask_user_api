import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 基础
    SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DEBUG = False
    TESTING = False
    # 数据库
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.getenv('JWT_EXPIRES', 24)))

config = Config()