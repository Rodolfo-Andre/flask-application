from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify
from app.models.pet import Pet
from app.schemas.pet import pets_schema, pet_query_schema, pet_schema
from app import db

bp = Blueprint("pet_api", __name__)

@bp.route("/")
class Pets(MethodView):
    @bp.arguments(pet_query_schema, location="query")
    @bp.response(200, pets_schema)
    def get(self, query):
        """Listado de mascota"""
        pets = Pet.query.order_by(Pet.birth_date.desc(), Pet.name.desc(), Pet.owner_name.desc()).all()
  
        if "owner_dni" in query.keys():
          pets = Pet.query.filter(Pet.owner_dni == query["owner_dni"])
        
        return pets
    
    @bp.arguments(pet_schema)
    @bp.response(201, pet_schema)
    def post(self, new_data):
        """Agregando mascota"""
        db.session.add(new_data)
        db.session.commit()

        return new_data