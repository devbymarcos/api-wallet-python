from flask import Blueprint, jsonify, Response, request
from models.users import Users


auth_bp = Blueprint('auth',__name__)

@auth_bp.post("/login")
def auht_user():
    
    #validar aqui
    email = request.form.get("email")
    user = Users.query.filter_by(email=email).first()

    if user : 
        user_data={
            "id":user.id,
            "first_name":user.first_name,
            "last_name" : user.last_name,
            "email": user.email,
            "photo": user.photo,
            "password":user.password
        }
    else:
        return 