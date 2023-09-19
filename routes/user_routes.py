from flask import Blueprint, jsonify, Response
from models.users import Users
import json


user_bp = Blueprint('user',__name__)

@user_bp.get("/users")
def find_users():     
    users = Users.query.all()
    user_list =[]
    for user in users:
        user_data={
            "id":user.id,
            "first_name":user.first_name,
            "last_name" : user.last_name,
            "email": user.email,
            "photo": user.photo
        }
        user_list.append(user_data)
    return jsonify(user_list)

@user_bp.get("/user/<int:id>")
def  find_user(id):
    user = Users.query.get(id)

    if user: 
        user_data={
            "id":user.id,
            "first_name":user.first_name,
            "last_name" : user.last_name,
            "email": user.email,
            "photo": user.photo
        }

        return jsonify(user_data)
    else:
        error_message = {"message": "usuário não encontrado" }
        response = Response(json.dumps(error_message),status=404,mimetype='application/json')
        return response
    
