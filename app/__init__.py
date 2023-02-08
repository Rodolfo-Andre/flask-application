from dotenv import load_dotenv 
load_dotenv()

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models.breed import Breed
    from .models.pet import Pet
 
    with app.app_context():  
      from app.blueprints.pet import bp

      app.register_blueprint(bp)
  
    return app