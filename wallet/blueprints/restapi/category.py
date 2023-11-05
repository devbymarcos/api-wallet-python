from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.ext.database import db


class CategoryResource(Resource):
    def get(self):
        return jsonify({"message": "buscando pelo id"})


class CategoriesResource(Resource):
    def get(self):
        return jsonify({"message": "buscando todos os registros"})
