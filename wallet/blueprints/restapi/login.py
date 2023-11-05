from flask import abort, jsonify, request
from flask_restful import Resource
from wallet.models.User import User
from wallet.ext.database import db


class LoginResource(Resource):
    pass
