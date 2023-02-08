from flask import Blueprint, render_template, flash, request 
from app.models.breed import Breed
from app.models.pet import Pet
from app.forms.pet_form import PetForm
from sqlalchemy import asc
from app import db

bp = Blueprint('pet', __name__, template_folder='templates')

@bp.route('/')
def index():
  pets = Pet.query.order_by(Pet.birth_date.desc(), Pet.name.desc(), Pet.owner_name.desc()).all()

  return render_template('index.html', pets=pets)  

@bp.route('/pet', methods=['GET', 'POST'])
def add_pet():
  pet_form = PetForm()

  if request.method == "POST" and pet_form.validate_on_submit():
    pet_data = pet_form.data
    pet_data.popitem()

    pet_object = Pet(**pet_data)

    db.session.add(pet_object)
    db.session.commit()

    flash("Se ha registrado la mascota con éxito")
    return render_template('index.html')

  return render_template('add_pet.html', form=pet_form)

@bp.route('/pet/<int:id>', methods=['GET'])
def detail_pet(id):
  pet_object = Pet.query.get_or_404(id)

  return render_template("detail_pet.html", pet=pet_object)




