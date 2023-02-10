from app import ma
from app.models.breed import Breed
from marshmallow import fields, validate

class BreedSchema(ma.SQLAlchemySchema):
  class Meta:
    model = Breed
    load_instance = True
    dump_only = ("id",)
    
  id = ma.auto_field()
  name = fields.String(required=True, validate=validate.Length(min=3, max=20))

breed_schema = BreedSchema()
breeds_schemas = BreedSchema(many=True)