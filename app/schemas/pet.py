from app import ma
from app.models.pet import Pet
from marshmallow import fields, validate, Schema

class PetSchema(ma.SQLAlchemySchema):
  class Meta: 
    model = Pet
    load_instance = True
    dump_only = ("updated_at", "created_at", "id")

  id = ma.auto_field()
  name = fields.String(validate=validate.Length(min=3, max=20))
  owner_dni = fields.String(validate=validate.Regexp("^[0-9]{8}$"))
  owner_name = fields.String(validate=validate.Length(min=3, max=30))
  birth_date = fields.Date()
  created_at = ma.auto_field()
  updated_at = ma.auto_field()
  breed_id = fields.Integer(required=True, validate=validate.Range(min=1))

class PetQueryArgsShema(Schema):
  owner_dni = fields.String()

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)
pet_update_schema = PetSchema(load_instance=False)
pet_query_schema = PetQueryArgsShema()
