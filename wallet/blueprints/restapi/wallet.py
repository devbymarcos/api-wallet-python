from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.models.Wallet import Wallet
from wallet.blueprints.restapi.verify_auth import auth
from wallet.functions.helpers import api_format_return

class WalletIdResource(Resource):

    def get(self, id):
        wallet = Wallet(id=id)
        data = wallet.find_by_id()

        if data is not None:
            data_result = {
                'id': data.id,
                'name': data.name,
                'description': data.description,
                'option_wallet': data.option_wallet
            }
            return jsonify(api_format_return([data_result],request="wallet"))

    def delete(self, id):
        wallet = Wallet(id=id)
        data = wallet.remove()
        if not data:
            return jsonify(api_format_return(message="Não foi possivel fazer exclusão",request="wallet",data_items=False))


        return jsonify(api_format_return(message="exclusao realizda",request="wallet",data_items=False))
    
     
    

class WalletResource(Resource):
    #TODO passar o user id 
    def get(self):
        wallet = Wallet(user_id=1)
        data = wallet.find_all()

        if data :
            data_result = [{
                    'id':  wallet[0].id,
                    'name': wallet[0].name,
                    'description': wallet[0].description,
                    'option_wallet': wallet[0].option_wallet} for wallet in data
            ]
             
            return jsonify(api_format_return(data_result,request="wallet"))

        else:
            return jsonify(api_format_return(False,message="Não encontramos resultados",request="wallet"))
        

       


    def post(self):
        if request.is_json:
            data_json = request.get_json()
            wallet = Wallet(
                user_id=1,
                name=data_json['name'],
                description=data_json["description"],
                option_wallet=data_json["option_wallet"]
            )
            data = wallet.save()

            if data:
                data_result = {
                    "id": wallet.id,
                    'name': wallet.name,
                    'description': wallet.description,
                    'option_wallet': wallet.option_wallet
                }

                return jsonify(api_format_return(data_result,request="wallet"))
            else:
                return jsonify(api_format_return(None,message="Algo deu erra contate o admin",request="wallet"))
            
    def put(self):
        if request.is_json:
            data_json = request.get_json()
            wallet = Wallet(
                user_id=1,
                name=data_json['name'],
                description=data_json["description"],
                option_wallet=data_json["option_wallet"]
            )

            data = wallet.save()

            if data:
                data_result = {
                    "id": wallet.id,
                    'name': wallet.name,
                    'description': wallet.description,
                    'option_wallet': wallet.option_wallet
                }

                return jsonify(api_format_return([data_result],request="wallet"))
            else:
                return jsonify(api_format_return(None,message="Algo deu erra contate o admin",request="wallet"))



