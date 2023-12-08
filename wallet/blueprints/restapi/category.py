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

    def delete(self, id):
        delete = Category.remove(id)
        if delete:
            return jsonify({"message": "Dados removido", "execute": True})
        else:
            return jsonify({"message": "Algo ddeu errado não foi possível remover os dados", "execute": False})

    def put(self, id):
        pass


class CategoriesResource(Resource):
    def get(self):
        result = Category.find_all(user_id=1)
        if (result == None):
            return jsonify({"message": "não encontramos o registro ", "data": None})

        data_result = [
            {'id': category[0].id,
             'name': category[0].name,
             'description': category[0].description,
             'type': category[0].type} for category in result
        ]
        return jsonify({"category": data_result})


class CategoryCreate(Resource):
    def post(self):
        if request.is_json:
            data = request.get_json()

            category = Category.save(
                user_id=data['user_id'],
                name=data['name'],
                description=data['description'],
                type=data['type'])

            if category != False:
                data_result = {
                    'id': category.id,
                    'user_id': category.user_id,
                    'name': category.name,
                    'description': category.description,
                    "type": category.type

                }

                return jsonify({"category": data_result})
            else:
                return jsonify({'message': 'Nào foi possível criar a carteira', 'execute': False})
