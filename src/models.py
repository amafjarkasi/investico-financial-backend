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
    question_1 = db.Column(db.String(120), unique=False, nullable=True)
    question_2 = db.Column(db.String(120), unique=False, nullable=True)
    question_3 = db.Column(db.String(120), unique=False, nullable=True)
    question_4 = db.Column(db.String(120), unique=False, nullable=True)
    question_5 = db.Column(db.String(120), unique=False, nullable=True)
    

    # relationships
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return '<Portfolio %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "question_1": self.question_1,
            "question_2": self.question_2,
            "question_3": self.question_3,
            "question_4": self.question_4,
            "question_5": self.question_5,
        }
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(120), unique=False, nullable=True)
    quantity = db.Column(db.String(120), unique=False, nullable=True)
    symbol = db.Column(db.String(120), unique=False, nullable=True)
    total_purchase = db.Column(db.String(120), unique=False, nullable=True)
    date = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Transaction %r>' % self.symbol

    def serialize(self):
        return {
            "id": self.id,
            "price": self.price,
            "quantity": self.quantity,
            "symbol": self.symbol,
            "total_purchase": self.total_purchase,
            "date": self.date
        }

     # relationships
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question1 = db.Column(db.String(120), unique=False, nullable=True)
    question2 = db.Column(db.String(120), unique=False, nullable=True)
    question3 = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Profile %r>' % self.id

    def serialize(self):
        return {
            "question1": self.question1,
            "question2": self.question2,
            "question3": self.question3

        }