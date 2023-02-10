from dotenv import load_dotenv 
load_dotenv()

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_smorest import Api
from app.config import Config

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
smorest_api = Api()
ma = Marshmallow()

def create_app():
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    
    ma.init_app(app)
    smorest_api.init_app(app)

    from .models.breed import Breed
    from .models.pet import Pet
 
    with app.app_context():  
      from app.blueprints.pet import bp
      from app.blueprints.pet_api import bp as pet_api_bp
      from app.blueprints.breed_api import bp as breed_api_bp

      app.register_blueprint(bp)
      smorest_api.register_blueprint(pet_api_bp, url_prefix="/pet-api", name="Api de Mascotas")  
      smorest_api.register_blueprint(breed_api_bp, url_prefix="/breed-api", name="Api de Razas")
    return app

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages_error/404.html'), 404
