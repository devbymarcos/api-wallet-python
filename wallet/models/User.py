from wallet.ext.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date, func, ForeignKey

from wallet.ext.database import db


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    photo = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(),
                        onupdate=func.current_timestamp())

    def get_user_id(self, id):
        user = db.session.execute(
            db.select(User).filter_by(id=id)).scalar_one()
        if user is not None:
            return user
        else:
            return None

    def add(self, user):
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
