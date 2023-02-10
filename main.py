from app import create_app
from app.helpers.breed_helper import BreedHelper
from app.models.breed import Breed

app = create_app()

with app.app_context(): 
 if Breed.query.count() == 0:
    BreedHelper.add_dummy_breed_data(BreedHelper.get_data_json())

if __name__ == '__main__':
    app.debug = True
    app.run()