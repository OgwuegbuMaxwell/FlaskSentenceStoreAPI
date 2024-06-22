from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import os
from pymongo import MongoClient
import bcrypt

# Initialize Flask and Flask-RESTful extension
app = Flask(__name__)
api = Api(app)

# Connect to MongoDB using MongoClient
client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]


def verifyUser(username):
    # Check if the user exists in the database
    user_data = users.find_one({"Username": username})
    if not user_data:
        return False
    return True

# Helper function to verify the hashed password
def verifyPassword(username, password):
    user_data = users.find_one({"Username": username})  # Retrieves a single document
    if user_data:
        hashed_password = user_data["Password"]
        if bcrypt.hashpw(password.encode('utf8'), hashed_password) == hashed_password:
            return True
    return False

# Helper function to retrieve the token count for a user
def countTokens(username):
    user_data = users.find_one({"Username": username})  # Retrieves a single document
    if user_data:
        tokens = user_data["Token"]
        return tokens
    return 0  # Default token count if user is not found

# Resource to handle user registration
class Register(Resource):
    def post(self):
        postedData = request.get_json()  # Get data posted by the user
        username = postedData["username"]
        password = postedData["password"]
        
        # Check if the username already exists in the database
        if users.find_one({"Username": username}):
            retJson = {
                "status": 301,
                "msg": "Username already exists. Please choose a different username."
            }
            return jsonify(retJson)
        
        # Hash the password for storage
        hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        
        # Insert the new user into the database
        users.insert_one({
            "Username": username,
            "Password": hashed_password,
            "Sentence": "",
            "Token": 10  # Each new user starts with 10 tokens
        })
        
        # Return a success message
        retJson = {
            "status": 200,
            "msg": "You have successfully signed up for the API"
        }
        return jsonify(retJson)


# Resource to store a sentence in the database
class Store(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]
        
        # Verify Username
        user_exist = verifyUser(username)
        if not user_exist:
            retJson = {
                "status": 302, 
                "msg": "Invalid Credentials",
            }
            return jsonify(retJson)
            
        
        # Verify user password
        correct_password = verifyPassword(username, password)
        if not correct_password:
            # Incorrect password
            retJson = {
                "status": 302,
                "msg": "Invalid Credentials"
            }  
            return jsonify(retJson)
        
        # Check if the user has enough tokens
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            # Insufficient tokens
            retJson = {
                "status": 301,
                "msg": "Insufficient token"
            }
            return jsonify(retJson) 
        
        # Store the sentence and decrement the token count
        users.update_one(
            {"Username": username},
            {"$set": {"Sentence": sentence, "Token": num_tokens - 1}}
        )
        
        # Return success message
        retJson = {
            "status": 200, "msg": "Sentence saved successfully!"
        }
        
        return jsonify(retJson)


class Token(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData.get("username")
        password = postedData.get("password")
        
        # Verify Username
        user_exist = verifyUser(username)
        if not user_exist:
            retJson = {
                "status": 302, 
                "msg": "Invalid Credentials",
            }
            return jsonify(retJson)
            

        # Verify user password
        correct_password = verifyPassword(username, password)
        if not correct_password:
            retJson = {
                "status": 302, 
                "msg": "Invalid Credentials",
            }
            return jsonify(retJson)

        # Retrieve the token count for the user
        num_tokens = countTokens(username)
        if num_tokens is None:
            retJson = {
                "status": 404, 
                "msg": "User not found"
            }

        # Return the number of tokens
        retJson = {
            "status": 200, 
            "msg": f"You have {num_tokens} tokens remaining."
        }
        
        return jsonify(retJson)


class Get(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData.get("username")
        password = postedData.get("password")
        
        # Verify Username
        user_exist = verifyUser(username)
        if not user_exist:
            retJson = {
                "status": 302, 
                "msg": "Invalid Credentials",
            }
            return jsonify(retJson)
            

        # Verify user password
        correct_password = verifyPassword(username, password)
        if not correct_password:
            retJson = {
                "status": 302, 
                "msg": "Invalid Credentials",
            }
            return jsonify(retJson)

        # Retrieve the token count for the user
        num_tokens = countTokens(username)
        if num_tokens <=0 :
            retJson = {
                "status": 301, 
                "msg": "Hey! you need to buy extra token"
            }
            return jsonify(retJson)

        # Charge the user a token for making this request
        users.update_one(
            {"Username": username},
            {"$set": {"Token": num_tokens - 1}}
        )

        # Retrieve Sentence
        user_data = users.find_one({"Username": username})
        sentence = user_data["Sentence"]
        
        
        retJson = {
            "status": 200, 
            "Sentence": sentence
        }
        
        return jsonify(retJson)



# Add the resources to the API
api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Token, '/tokens')
api.add_resource(Get, '/get')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)







