from app.helpers.breed_helper import BreedHelper

def test_get_data_json():
  assert BreedHelper.get_data_json().__len__() == 10