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
        return '<User %r>' % self.email

    def validate_password(self, password):
      if self.password != password:
          return False

      return True

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password,
            # do not serialize the password, its a security breach
        }
        
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_1 = db.Column(db.String(120), unique=False, nullable=False)
    question_2 = db.Column(db.String(120), unique=False, nullable=False)
    question_3 = db.Column(db.String(120), unique=False, nullable=False)
    question_4 = db.Column(db.String(120), unique=False, nullable=False)
    question_5 = db.Column(db.String(120), unique=False, nullable=False)
    

    # relationships
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#     # def __repr__(self):
#     #     return '<Portfolio %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id
#         }