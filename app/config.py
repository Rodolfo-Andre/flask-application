import os

class Config: 
    SECRET_KEY = os.environ.get("SECRET_KEY") or "SECRET"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "mysql://root:root@localhost/app"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or False