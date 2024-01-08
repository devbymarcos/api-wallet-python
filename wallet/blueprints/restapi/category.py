from flask import jsonify, request
from flask_restful import Resource
from wallet.ext.database import db
from wallet.models.Category import Category
from wallet.functions.helpers import api_format_return

class CategoryIdResource(Resource):
    def get(self, id):
        category = Category(id=id)
        category_result = category.find_by_id()

        if category_result is not None:
            data_result = {
                'name': category_result.name,
                'description': category_result.description,
                'type': category_result.type
            }
            return jsonify(api_format_return(
                data=[data_result],
                request="/category"))

        return jsonify(api_format_return(
            message="Não encontramos dados", 
            request="/category",
            data_items=False))

    def delete(self, id):
        category = Category(id=id)
        delete = category.remove()
        if delete:
            return jsonify(api_format_return(
                message="Removido", 
                data_items=True))
        else:
            return jsonify(api_format_return(
                message="Algo deu errado contate o Admin",
                data_items=False,
                request="/category"))

    


class CategoriesResource(Resource):
    #TODO PASSAR ID DO USER
    def get(self):
        category = Category(user_id=1)
        data = category.find_all()
        if (data == None):
            return jsonify(api_format_return(
                data_items=False, 
                message="Não encontramos dados", 
                request="/categories"))

        data_result = [
            {'id': category[0].id,
             'name': category[0].name,
             'description': category[0].description,
             'type': category[0].type} for category in data
        ]
        return jsonify(api_format_return(
            data=data_result,
            message="Não encontramos dados",
            request="categories"))
    
    def post(self):
        if request.is_json:
            data = request.get_json()
            category = Category(
                user_id=data['user_id'],
                name=data['name'],
                description=data['description'],
                type=data['type'])
            create = category.save()
            if create:
                data_result = {
                    'id': create.id,
                    'user_id': create.user_id,
                    'name': create.name,
                    'description': create.description,
                    "type": create.type

                }

                return jsonify(api_format_return(
                    data=[data_result],
                    request="/category",
                    data_items=True,
                    ))
            else:
                return jsonify(api_format_return(message="Nào foi possível criar a carteira",request="/category",
                    data_items=False,))

    def put(self):
        category = request.get_json()
        
        category = Category(
            id=category['id'],
            name=category['name'],
            description=category['description'],
            type=category['type'])
        update = category.update()
       
        if update:
            data_result = {
                    'id': update.id,
                    'user_id': update.user_id,
                    'name': update.name,
                    'description': update.description,
                    "type": update.type

                }
            return jsonify(api_format_return(
                data=[data_result],
                message="atualizado com sucesso",
                request="/gategory",
                data_items=True))
        else:
            return jsonify(api_format_return(message="Não foi possivel atualizar contate o admin", request="/category", data_items=False))
        

   