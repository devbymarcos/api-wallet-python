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

    @classmethod
    def find_all(cls, user_id):
        categories = db.session.execute(
            db.select(cls).filter_by(user_id=user_id)).all()
        return categories

    @classmethod
    def find_by_id(cls, category_id):
        try:
            category = db.session.execute(
                db.select(cls).filter_by(id=category_id)).scalar_one()

        except Exception as e:
            print(e)
            return None

        return category

    @classmethod
    def save(cls, user_id, name, description, type,):
        category_create = cls(
            user_id=user_id,
            name=name,
            description=description,
            type=type
        )
        try:
            db.session.add(category_create)
            db.session.commit()
            return category_create
        except Exception as e:
            print(e)
            return False
    
    @classmethod
    def update(cls,id,name, description, type):
        category_update = cls.find_by_id(id)
        if category_update:
            try:
                category_update.name = name
                category_update.description = description
                category_update.type = type
                
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                print(e)
                return False
        else:
            return False