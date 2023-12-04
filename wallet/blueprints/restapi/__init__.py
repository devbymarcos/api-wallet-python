from flask import Blueprint
from flask_restful import Api
from .user import UserResource
from .wallet import WalletResource, WalletsResource,WalletPostResource
from .login import LoginResource
from .invoice import InvoiceResource, InvoicesResource
from .category import CategoriesResource, CategoryResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(LoginResource, "/Login/")
    api.add_resource(UserResource, "/user")
    api.add_resource(WalletsResource, "/wallets/")
    api.add_resource(WalletResource, "/wallet/<int:id>")
    api.add_resource(WalletPostResource,"/wallet")
    api.add_resource(InvoiceResource, "/invoice/")
    api.add_resource(InvoicesResource, "/invoices/")
    api.add_resource(CategoryResource, "/category/")
    api.add_resource(CategoriesResource, "/categories/")
    app.register_blueprint(bp)
