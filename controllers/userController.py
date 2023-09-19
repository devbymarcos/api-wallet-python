
from database import get_session, User

def get_all_users():
    session = get_session()
    users = session.query(User).all()
