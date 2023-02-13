from dotenv import load_dotenv 
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_smorest import Api
from flask_limiter import Limiter, HEADERS
from flask_limiter.util import get_remote_address
from app.config import Config
from enum import Enum

class Limits(Enum):
    PER_DAY_100 = "100/day"
    PER_DAY_10 = "10/day"

db = SQLAlchemy()
migrate = Migrate()
smorest_api = Api()
ma = Marshmallow()
limiter = Limiter(key_func=get_remote_address, default_limits=[Limits.PER_DAY_100.value],
                  headers_enabled=True,
                  header_name_mapping={
     HEADERS.LIMIT : "X-My-Limit",
     HEADERS.RESET : "X-My-Reset",
     HEADERS.REMAINING: "X-My-Remaining"})

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    
    ma.init_app(app)
    smorest_api.init_app(app)

    limiter.init_app(app)

    from app.models.breed import Breed
    from app.models.pet import Pet
 
    with app.app_context():          
      from app.blueprints.pet import bp
      from app.blueprints.pet_api import bp as pet_api_bp
      from app.blueprints.breed_api import bp as breed_api_bp

      app.register_blueprint(bp)
      smorest_api.register_blueprint(pet_api_bp, url_prefix="/pet-api", name="Api de Mascotas")  
      smorest_api.register_blueprint(breed_api_bp, url_prefix="/breed-api", name="Api de Razas")
      
      limiter.limit(Limits.PER_DAY_10.value, methods=["POST"])(bp)
      limiter.limit(Limits.PER_DAY_10.value, methods=["POST", "PUT", "DELETE"])(pet_api_bp)
      limiter.limit(Limits.PER_DAY_10.value, methods=["POST"])(breed_api_bp)
    
      from app.errors import page_not_found, too_many_requests
      app.register_error_handler(404, page_not_found)
      app.register_error_handler(429, too_many_requests)
      
    return app