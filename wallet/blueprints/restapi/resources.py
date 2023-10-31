from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.models.User import User
from wallet.ext.database import db


class UserResource(Resource):
    def get(self):
        user = User()
        user_list = user.get_user_id(1)

        if user_list is not None:
            return jsonify({
                "id": user_list.id,
                "first_name": user_list.first_name,
                "last_name": user_list.last_name,
                "email": user_list.email
            })

    def post(self):
        data = request.get_json()
        user = User()
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        user.password = data["password"]
        user.photo = 'default'
        user.add(user)

        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "photo": user.photo

        }
        return jsonify(user_data)


class WalletResource(Resource):
    def get(self):
        return jsonify({"message": "carteira aqui "})


class LoginResource(Resource):
    pass
