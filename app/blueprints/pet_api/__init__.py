from flask_smorest import Blueprint
from flask.views import MethodView
from flask import jsonify
from app.models.pet import Pet
from app.schemas.pet import pets_schema, pet_query_schema, pet_schema, pet_update_schema
from app import db
import datetime

class PetMessageCode ():
    NOT_FOUND = "La mascota no existe"

bp = Blueprint("pet_api", __name__)

@bp.route("/")
class Pets(MethodView):
    @bp.arguments(pet_query_schema, location="query")
    @bp.response(200, pets_schema)
    def get(self, query):
        """Listar mascota"""
        pets = Pet.query.order_by(Pet.birth_date.desc(), Pet.name.desc(), Pet.owner_name.desc()).all()
  
        if "owner_dni" in query.keys():
          pets = Pet.query.filter(Pet.owner_dni == query["owner_dni"])
        
        return pets
    
    @bp.arguments(pet_schema)
    @bp.response(201, pet_schema)
    def post(self, new_data):
        """Agregar mascota"""
        db.session.add(new_data)
        db.session.commit()

        return new_data

@bp.route("/<int:id>")
class PetsById(MethodView):
    @bp.response(200, pet_schema)
    def get(self, id):
        """Obtener mascota por id"""
        pet = Pet.query.get(id)

        if pet is None:
          return jsonify({"message": PetMessageCode.NOT_FOUND}), 404
      
        return pet
    
    @bp.arguments(pet_update_schema)
    @bp.response(200, pet_schema)
    def put(self, data, id):
      """Actualizar mascota por id"""
      pet = Pet.query.get(id)

      if pet is None:
        return jsonify({"message": PetMessageCode.NOT_FOUND}), 404

      pet.from_dict(**data)
      pet.updated_at = datetime.datetime.now()

      db.session.add(pet)
      db.session.commit()

      return pet

    @bp.response(200)
    def delete(self, id):
      """Eliminar mascota por id"""
      pet = Pet.query.get(id)
    
      if pet is None:
        return jsonify({"message": PetMessageCode.NOT_FOUND}), 404
      
      db.session.delete(pet)
      db.session.commit()

      return jsonify({"message": "Mascota eliminada con éxito"})