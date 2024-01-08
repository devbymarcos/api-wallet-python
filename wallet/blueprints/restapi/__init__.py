from flask import Blueprint
from flask_restful import Api
from .user import UserResource
from .wallet import WalletResource, WalletIdResource
from .login import LoginResource
from .invoice import InvoiceResource, InvoicesResource
from .category import CategoriesResource, CategoryResource, CategoryCreate

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(LoginResource, "/Login/")
    api.add_resource(UserResource, "/user")
    api.add_resource(WalletIdResource, "/wallet/<int:id>")
    api.add_resource(WalletResource, "/wallet")
    api.add_resource(InvoiceResource, "/invoice/")
    api.add_resource(InvoicesResource, "/invoice/<int:id>")
    api.add_resource(CategoryResource, "/category/<int:id>")
    api.add_resource(CategoriesResource, "/categories/")
    api.add_resource(CategoryCreate, "/category")
    app.register_blueprint(bp)
