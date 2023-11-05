from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.models.User import User
from wallet.ext.database import db


class WalletResource(Resource):
    def get(self):
        return jsonify({"message": "carteira aqui "})


class WalletsResource(Resource):
    def get(self):
        return jsonify({"message": "todas as carteiras"})
