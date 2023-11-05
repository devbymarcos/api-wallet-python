from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.ext.database import db


class InvoiceResource(Resource):
    def get(self):
        return jsonify({"message": "buscando um invoice single"})


class InvoicesResource(Resource):
    def get(self):
        return jsonify({"message": "todas as invoices"})
