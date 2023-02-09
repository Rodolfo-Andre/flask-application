from app import ma
from app.models.pet import Pet
import marshmallow

class PetSchema(ma.SQLAlchemySchema):
  class Meta: 
    model = Pet
    load_instance = True
    dump_only = ("updated_at", "created_at", "id")

  id = ma.auto_field()
  name = ma.auto_field()
  owner_dni = ma.auto_field()
  owner_name = ma.auto_field()
  birth_date = ma.auto_field()
  created_at = ma.auto_field()
  updated_at = ma.auto_field()
  breed_id = ma.auto_field()

class PetQueryArgsShema(marshmallow.Schema):
  owner_dni = marshmallow.fields.String()

pet_schema = PetSchema()
pets_schema = PetSchema(many=True)
pet_update_schema = PetSchema(load_instance=False)
pet_query_schema = PetQueryArgsShema()
