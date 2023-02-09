from flask import Blueprint, render_template, flash, request, url_for, redirect
from app.models.pet import Pet
from app.forms.pet_form import PetForm
from app import db
import datetime

bp = Blueprint('pet', __name__, template_folder='templates')

@bp.route('/')
def index():
  owner_dni = request.args.get("owner_dni")
  pets = Pet.query.order_by(Pet.birth_date.desc(), Pet.name.desc(), Pet.owner_name.desc()).all()
  owners = [ { "owner_dni": pet.owner_dni, "owner_name": pet.owner_name } for pet in pets ]

  if owner_dni :
    pets = Pet.query.filter(Pet.owner_dni == owner_dni)
  
  return render_template('index.html', pets=pets, owners=owners, selected_owner=owner_dni)  

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
    return redirect(url_for("pet.index"))

  return render_template('add_pet.html', form=pet_form)

@bp.route('/pet/<int:id>', methods=['GET'])
def detail_pet(id):
  pet_object = Pet.query.get_or_404(id)

  return render_template("detail_pet.html", pet=pet_object)

@bp.route('/pet/<int:id>/update', methods=['GET', "POST"])
def update_pet(id):
  pet_object = Pet.query.get_or_404(id)

  pet_form = PetForm()
  
  if request.method == "POST" and pet_form.validate_on_submit():
    pet_data = pet_form.data
    pet_data.popitem()

    pet_object.from_dict(**pet_data)
    pet_object.updated_at = datetime.datetime.now()
    db.session.commit()
    
    flash("Se actualizaron los datos de la mascota con éxito")

  for field in pet_form:
    if (field.name != "csrf_token"):
      field.data = getattr(pet_object, field.name)

  return render_template("update_pet.html", form=pet_form, id=id)

@bp.route('/pet/<int:id>/delete', methods=['GET'])
def delete_pet(id):
  pet_object = Pet.query.get_or_404(id)

  db.session.delete(pet_object)
  db.session.commit()

  flash("Se ha eliminado a la mascota con éxito")

  return redirect(url_for("pet.index"))





