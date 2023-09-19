
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


def set_user(data):

    user = Users.query.filter_by(email=data['email']).first()

    if user:
        return Response(json.dumps({"message": "Este usuário ja existe"}))

    else:

        salt = bcrypt.gensalt()
        hash_passwd = bcrypt.hashpw(data['password'].encode('utf-8'), salt)
        try:
            user_add = Users(
                first_name="lopes",
                last_name="juvencio",
                email=data['email'],
                password=hash_passwd,
                photo="default"
            )

            db.session.add(user_add)
            db.session.commit()

            return Response(json.dumps({"messagem": "Usuário criado"}), status=200, mimetype='application/json')
        except Exception:
            print(Exception)
