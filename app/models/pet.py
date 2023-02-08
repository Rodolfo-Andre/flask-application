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
