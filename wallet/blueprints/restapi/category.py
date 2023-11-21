from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.ext.database import db
from wallet.models.Category import Category


class CategoryResource(Resource):
    def get(self, wallet_id):
        return jsonify({"message": "buscando pelo id"})


class CategoriesResource(Resource):
    def get(self):
        categories = Category()

        return jsonify(categories.find_all(1))
