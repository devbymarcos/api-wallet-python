from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.models.Wallet import Wallet
from wallet.ext.database import db
import json


class WalletResource(Resource):
    def get(self, id):
        wallet_result = Wallet.find_by_id(id)
        if wallet_result is not None:
            return jsonify({
                'name': wallet_result.name,
                'description': wallet_result.description
            })

        return jsonify({"message": "carteira aqui ", "id": id})

    def delete(self, id):
        wallet_result = Wallet.remove(id)
        if not wallet_result:
            return jsonify({"messagem": "Não foi possivel fazer exclusão", "execute": False})
        return jsonify({"message": "exclusao realizda", "execute": True})


class WalletsResource(Resource):
    def get(self):
        wallets = Wallet()
        result = wallets.find_all(user_id=1)
        if (result == None):
            return result

        data_result = [
            {'name': wallet[0].name, 'description': wallet[0].description} for wallet in result
        ]
        return jsonify(data_result)
