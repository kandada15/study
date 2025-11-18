from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
  app = Flask(__name__)

  db_config = {
    'user' : "test_user",
    'password' : "test_password",
    'host' : "localhost",
    'db_name' : "test_db"
  }

  # MySQLに接続するための情報
  app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4'.format(**db_config),
    # 追跡機能を無効
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  )

  db.init_app(app)
  return app

  

