
from flask import Blueprint, jsonify, Response
from models.users import Users, db
import json
import bcrypt


def find_user(id):
    user = Users.query.get(id)

    if user:
        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "photo": user.photo
        }

        return jsonify(user_data)
    else:
        error_message = {"message": "usuário não encontrado"}
        response = Response(json.dumps(error_message),
                            status=404, mimetype='application/json')
        return response


def find_users():
    users = Users.query.all()
    user_list = []
    for user in users:
        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "photo": user.photo
        }
        user_list.append(user_data)
    return jsonify(user_list)


def set_user(email, password):

    user = Users.query.filter_by(email=email).first()

    if user:
        return Response(json.dumps({"message": "Este usuário ja existe"}))
    else:

        salt = bcrypt.gensalt()
        hash_passwd = bcrypt.hashpw(password.encode('utf-8'), salt)

        user_add = Users(
            first_name="lopes",
            last_name="juvencio",
            email=email,
            password=hash_passwd,
            photo="default"
        )

        db.session.add(user_add)
        db.session.commit()

    return Response(json.dumps({"email": email, "senha": "feito"}), status=200, mimetype='application/json')
