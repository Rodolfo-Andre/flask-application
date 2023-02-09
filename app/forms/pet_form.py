from flask_wtf import FlaskForm
from app.models.breed import Breed
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField

class PetForm(FlaskForm):
  name = StringField('Nombre de la mascota: ', validators=[DataRequired("Ingrese el nombre de la mascota"), Length(max=20, message="El nombre de la mascota debe tener un máximo de 20 caracateres")])
  birth_date = DateField("Fecha de nacimiento de la mascota: ", validators=[DataRequired("Ingrese la fecha de nacimiento de la mascota")])
  owner_name = StringField('Nombre del propietario: ', validators=[DataRequired("Ingrese el nombre del propietario"), Length(max=30, message="El nombre del propietario debe tener un máximo de 30 caracateres")])
  owner_dni = StringField('Dni del propietario: ', validators=[DataRequired("Ingrese el dni del propietario"), Length(min=8, max=8, message="El dni debe de contener 8 dígitos")])
  breed = QuerySelectField("Selecciona la raza de la mascota: ", query_factory=lambda: Breed.query.all(), validators=[DataRequired("Selecciona una raza")], get_label="name")
