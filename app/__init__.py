from dotenv import load_dotenv 
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .blueprints.pet import bp
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(bp)
  
    return app