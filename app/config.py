import os

class Config: 
    SECRET_KEY = os.environ.get("SECRET_KEY") or "SECRET"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "mysql://root:root@localhost/app"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or False
    API_TITLE = os.environ.get("API_TITLE") or "Title"
    API_VERSION = os.environ.get("API_VERSION") or "v 0.0.1"
    OPENAPI_VERSION = os.environ.get("OPENAPI_VERSION") or "3.0.2"