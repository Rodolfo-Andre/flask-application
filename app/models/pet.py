from app import db
import datetime

class Pet(db.Model):
  __tablename__ = 'pet'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False)
  owner_dni = db.Column(db.String(8), unique=True, nullable=False)
  owner_name = db.Column(db.String(30), nullable=False)
  birth_date = db.Column(db.Date, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now())
  updated_at = db.Column(db.DateTime)
  breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'))
  breed = db.relationship("Breed", back_populates="pets", lazy='immediate')

  def to_dict(self):
    return {
      "name": self.name,
      "owner_dni": self.owner_dni,
      "owner_name": self.owner_name,
      "birth_date": self.birth_date,
      "created_at": self.created_at,
      "updated_at": self.updated_at,
      "breed": self.breed
    }

  def from_dict(self, **args):
    self.name = args["name"],
    self.owner_dni = args["owner_dni"]
    self.owner_name = args["owner_name"]
    self.birth_date = args["birth_date"]
    self.breed = args["breed"]
