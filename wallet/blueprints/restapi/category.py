from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.ext.database import db
from wallet.models.Category import Category


class CategoryResource(Resource):
     def get(self, id):
        category_result = Category.find_by_id(id)
        if category_result is not None:
            data_result = {
                'name': category_result.name,
                'description': category_result.description,
                'type': category_result.type
            }
            return jsonify({"category": data_result})

        return jsonify({"message": "não encontramos o resgistro ", "data": None})


class CategoriesResource(Resource):
    def get(self):
        result = Category.find_all(user_id=1)
        if (result == None):
            return jsonify({"message": "não encontramos o registro ", "data": None})

        data_result = [
            {'name': category[0].name,
             'description': category[0].description,
             'type': category[0].type} for category in result
        ]
        return jsonify({"category": data_result})
