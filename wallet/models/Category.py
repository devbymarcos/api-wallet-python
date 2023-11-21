from wallet.ext.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date, func, ForeignKey
from wallet.ext.database import db


class Category(Base):

    __tablename__ = "app_categories"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(),
                        onupdate=func.current_timestamp())

    def find_all(self, user_id):
        categories = db.session.execute(
            db.select(Category).filter_by(user_id=user_id)).all()
        return self.model_data(categories)

    def model_data(self, data):
        if (data == None):
            return data

        data_result = [
            {
                "name": item[0].name,
                "description": item[0].description,
                "type": item[0].type
            } for item in data
        ]
        return data_result
