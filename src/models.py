from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def validate_password(self, password):
      if self.password != password:
          return False

      return True

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
        
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # address = db.Column(db.String(80), unique=False, nullable=False)
    # weight = db.Column(db.Float, unique=False, nullable=False)
    # payment_id = db.Column(db.String(80), unique=True, nullable=False)
 
    

    # #relationships
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # def __repr__(self):
    #     return '<Order %r>' % self.id

    def serialize(self):
        return {
            "id": self.id
        }