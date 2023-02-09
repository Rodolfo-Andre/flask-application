import os

class Config: 
    SECRET_KEY = os.environ.get("SECRET_KEY") or "SECRET"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "mysql://root:root@localhost/app"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or False
    API_TITLE = os.environ.get("API_TITLE") or "Title"
    API_VERSION = os.environ.get("API_VERSION") or "v 0.0.1"
    OPENAPI_VERSION = os.environ.get("OPENAPI_VERSION") or "3.0.2"
    OPENAPI_URL_PREFIX = os.environ.get("OPENAPI_URL_PREFIX") or "/"
    OPENAPI_REDOC_PATH = os.environ.get("OPENAPI_REDOC_PATH")  or "/redoc"
    OPENAPI_REDOC_URL = os.environ.get("OPENAPI_REDOC_URL") or  "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    OPENAPI_SWAGGER_UI_PATH = os.environ.get("OPENAPI_SWAGGER_UI_PATH") or "/swagger-ui" 
    OPENAPI_SWAGGER_UI_URL = os.environ.get("OPENAPI_SWAGGER_UI_URL") or "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_RAPIDOC_PATH = os.environ.get("OPENAPI_RAPIDOC_PATH") or "/rapidoc"
    OPENAPI_RAPIDOC_URL= os.environ.get("OPENAPI RAPIDOC_PATH") or "https://unpkg.com/rapidoc/dist/rapidoc-min.js"