from flask import Blueprint, render_template, flash, request, url_for, redirect
from app.models.pet import Pet
from app.models.breed import Breed
from app.forms.pet_form import PetForm
from app import db
import datetime

bp = Blueprint('pet', __name__, template_folder='templates')

PER_PAGE = 5

@bp.route('/')
def index():
  owner_dni = request.args.get("owner_dni")
  page = request.args.get("page", 1, type=int)
  pets = Pet.query.order_by(Pet.birth_date.desc(), Pet.name.desc(), Pet.owner_name.desc()).paginate(page=page, per_page=PER_PAGE)
  owners = db.session.query(Pet.owner_name, Pet.owner_dni).distinct(Pet.owner_dni).all()

  owners_dict = [ { "owner_name": owner[0], "owner_dni": owner[1] } for owner in owners ]

  if owner_dni :
    pets = Pet.query.filter(Pet.owner_dni == owner_dni).paginate(page=page, per_page=PER_PAGE)
  
  return render_template('index.html', pets=pets, owners=owners_dict, selected_owner=owner_dni)  

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

@bp.route('/breed', methods=['POST'])
def add_breed():
  name = request.form["name"]
  url_origin = request.headers.__getitem__("Referer")

  if name.__len__() > 20 or name.strip() == "" :
    flash("Ocurrió un error al agregar la raza. Vuelve a intentarlo", "error")
    return redirect(url_origin)

  breed = Breed()
  breed.name = name

  flash("Raza añadida correctamente")

  db.session.add(breed)
  db.session.commit()

  return redirect(url_origin)
  



