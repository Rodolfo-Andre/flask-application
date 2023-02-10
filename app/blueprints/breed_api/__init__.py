from flask import jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from app.models.breed import Breed
from app.schemas.breed import breed_schema, breeds_schemas
from app import db

bp = Blueprint("breed_api", __name__)

PER_PAGE_DEFAULT = 5

@bp.route("/")
class Breeds(MethodView):
  @bp.response(200, breeds_schemas)
  @bp.paginate(page_size=PER_PAGE_DEFAULT)
  def get(self, pagination_parameters):
    """Listar razas"""
    breeds = Breed.query

    pagination_parameters.item_count = breeds.count()

    return breeds.paginate(page=pagination_parameters.page, per_page=pagination_parameters.page_size, error_out=True).items
    
  @bp.arguments(breed_schema)
  @bp.response(201, breed_schema)
  def post(self, new_data):
    """Agregar raza"""
    name = new_data.name

    if Breed.query.filter_by(name=name).all():
        return jsonify({ "message": "La raza ya está registrada"}), 422 

    breed = Breed()
    breed.name = name

    db.session.add(breed)
    db.session.commit()

    return breed