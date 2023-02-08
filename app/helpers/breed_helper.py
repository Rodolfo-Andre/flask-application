from app.models.breed import Breed
from app import db
import json

class BreedHelper:
    @staticmethod
    def add_dummy_breed_data(breeds):
        for breed in breeds:
            breed_object = Breed(**breed)
            db.session.add(breed_object)
            db.session.commit()
        print("Successfully added")
    
    @staticmethod
    def get_data_json():
      json_data = open("app/data/breed.json", encoding="UTF-8")
  
      data = json.load(json_data)

      json_data.close()

      return data
        