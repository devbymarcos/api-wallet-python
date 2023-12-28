from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.ext.database import db
from wallet.models.Invoice import Invoice


class InvoiceResource(Resource):
    def get(self):
        date = request.args.get("date")
        wallet_id = request.args.get("wallet_id")
        type = request.args.get("type")

        invoice  = Invoice()
        print(invoice)


        return jsonify({"message": "buscando um invoice single"})


class InvoicesResource(Resource):
    def get(self):
        return jsonify({"message": "todas as invoices"})
