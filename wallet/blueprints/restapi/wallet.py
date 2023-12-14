from flask import abort, jsonify, request
from flask_restful import Resource, reqparse
from wallet.models.Wallet import Wallet
from wallet.blueprints.restapi.verify_auth import auth


class WalletResource(Resource):

    def get(self, id):
        wallet_result = Wallet.find_by_id(id)
        if wallet_result is not None:
            data_result = {
                'id': wallet_result.id,
                'name': wallet_result.name,
                'description': wallet_result.description,
                'option_wallet': wallet_result.option_wallet
            }
            return jsonify({"wallet": data_result})

        return jsonify({"message": "não encontramos o resgistro ", "data": None})

    def delete(self, id):
        wallet_result = Wallet.remove(id)
        if not wallet_result:
            return jsonify({"messagem": "Não foi possivel fazer exclusão", "execute": False})
        return jsonify({"message": "exclusao realizda", "execute": True})


class WalletPostResource(Resource):
    def post(self):
        if request.is_json:
            data = request.get_json()

            wallet = Wallet.save(user_id=1,
                                 name=data['name'],
                                 description=data["description"],
                                 option_wallet=data["option_wallet"]
                                 )

            if wallet:
                data_result = {
                    "id": wallet.id,
                    'name': wallet.name,
                    'description': wallet.description,
                    'option_wallet': wallet.option_wallet
                }

                return jsonify({"wallet": data_result})
            else:
                return jsonify({'message': 'Nào foi possível criar a carteira', 'execute': False})


class WalletsResource(Resource):
    def get(self):
        result = Wallet.find_all(user_id=1)
        if result is None:
            return result

        data_result = [
            {
                'id':  wallet[0].id,
                'name': wallet[0].name,
                'description': wallet[0].description,
                'option_wallet': wallet[0].option_wallet} for wallet in result
        ]
        return jsonify({"wallets": data_result})
