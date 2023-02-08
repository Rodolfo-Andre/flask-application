from app import db

class Breed(db.Model):
  __tablename__ = 'breed'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False)
  pets = db.relationship('Pet', backref='breed', lazy='True')