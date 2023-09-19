from flask import Blueprint, request, Response, json


from controllers.userController import find_users, find_user, set_user


user_bp = Blueprint('user', __name__)


@user_bp.get("/users")
def route_users():
    result = find_users()
    return result


@user_bp.get("/user/<int:id>")
def route_user(id):
    result = find_user(id)
    return result


@user_bp.post("/user")
def route_user_post():
    if request.is_json:
        data = request.json
        response = set_user(data)
        return response
    else:
        Response(json.dumps({"message": "application/json"}))
