"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Portfolio, Transaction
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, current_user, get_jwt_identity
)

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Get all users endpoint
@app.route('/user', methods=['GET'])
def all_users():

    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_address(user_id):

    user1 = User.query.get(user_id)
    if user1 is None:
        raise APIException('User not found', status_code=404)


#Register endpoint
@app.route('/signup', methods=['POST'])
def signup():

    request_body_user = request.get_json()

    newuser = User(full_name=request_body_user["full_name"],
    email=request_body_user["email"], password=request_body_user["password"])
    db.session.add(newuser)
    db.session.commit()

    return "done", 200  

#Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    params = request.get_json()
    email = params.get('email', None)
    password = params.get('password', None)

    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    userquery = User.query.filter_by(email = email).first()
    if userquery is None:
        return jsonify({"msg": "user not found"}), 401
    if userquery.validate_password(password) is False:
        return jsonify({"msg": "invalid password"}), 401

     # Identity can be any data that is json serializable
    ret = {'jwt': create_access_token(identity=email), 'user': userquery.serialize()}
    return jsonify(ret), 200  

#portfolio questions
@app.route('/portfolio', methods=['GET'])
def all_portfolio():

    portfolio = Portfolio.query.all()
    all_portfolio = list(map(lambda x: x.serialize(), portfolio))

    return jsonify(all_portfolio), 200

# Get fields from Form Data
    
    
@app.route('/portfolio', methods=['POST'])
def portfolio():
    body = request.get_json()
    newportfolio = Portfolio(question_1=body['question1'], question_2=body['question2'], question_3=body['question3'], question_4=body['question4'], question_5=body['question5'])
    db.session.add(newportfolio)
    db.session.commit()
    return "done", 200  


# """
# Add new transaction 

# """

@app.route('/buy', methods=['POST', 'GET'])
def buy():

    # POST request
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'price' not in body:
            raise APIException("Missing price.", status_code=404)
        if 'quantity' not in body:
            raise APIException("Missing quantity", status_code=404)
        if 'symbol' not in body:
            raise APIException("Missing symbol.", status_code=404)
        if 'date' not in body:
            raise APIException("Missing date.", status_code=404)
        
        newbuy = Transaction(price=body['price'], quantity=body['quantity'], symbol=body['symbol'], date=body['date'],total_purchase=body['total_purchase'])
        db.session.add(newbuy)
        db.session.commit()      
        response_body = newbuy.serialize()       
        return jsonify(response_body), 200

    #GET request 
    if request.method == 'GET':
        newbuy = Transaction.query.all()
        newbuy = list(map(lambda x: x.serialize(), newbuy))
        return jsonify(newbuy), 200

    return "OK!", 200


    #  # Identity can be any data that is json serializable
    # ret = {'jwt': create_access_token(identity=email), 'user': userquery.serialize()}
    # return jsonify(ret), 200 



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
