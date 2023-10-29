from flask import abort, jsonify
from flask_restful import Resource


class UserResource(Resource):

    def get(self):
        return jsonify({"message": "oi com estamos "})


class WalletResource(Resource):
    pass
