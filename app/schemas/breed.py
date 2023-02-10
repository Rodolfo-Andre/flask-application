from app import ma
from app.models.breed import Breed

class BreedSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Breed
        load_instance = True
        dump_only = ("id")
    
    id = ma.auto_field()
    name = ma.auto_field()