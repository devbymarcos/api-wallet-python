from flask import Blueprint 


from controllers.userController import find_users, find_user 


user_bp = Blueprint('user',__name__)

@user_bp.get("/users")
def route_users():
    result = find_users()
    return result


@user_bp.get("/user/<int:id>")
def route_user(id):
    result = find_user(id)
    return result
    
