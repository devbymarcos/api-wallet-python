from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.models.Wallet import Wallet
from wallet.ext.database import db
import json


class WalletResource(Resource):
    def get(self):
        wallet = Wallet()
        wallet_result = wallet.find_by_id(2)
        if wallet_result is not None:
            return jsonify({
                'name': wallet_result.name,
                'description': wallet_result.description
            })

        return jsonify({"message": "carteira aqui "})


class WalletsResource(Resource):
    def get(self):
        wallets = Wallet()
        wallet_list = wallets.find_all_reduce(1)
        return jsonify(wallet_list)
