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

    def __init__(
            self,
            id=None, 
            user_id=None,
            name=None,
            description=None,
            type=None
            ):
        self.id = id
        self.user_id =user_id
        self.name = name
        self.description = description
        self.type = type

    def find_all(self):
        try:
            categories = db.session.execute(
                db.select(Category).filter_by(user_id=self.user_id)).all()
            return categories
        except Exception as e:
            print(e)
            return None

    def find_by_id(self):
        try:
            category = db.session.execute(
                db.select(Category).filter_by(id=self.id)).scalar_one()
            return category
        except Exception as e:
            print(e)
            return None

    def save(self):
        category = Category(
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            type=self.type
        )
        try:
            db.session.add(category)
            db.session.commit()
            return category
        except Exception as e:
            print(e)
            return False

    def update(self):
        category = self.find_by_id()
        if category:
            try:
                category.name = self.name
                category.description = self.description
                category.type = self.type
                db.session.commit()
                return category
            except Exception as e:
                db.session.rollback()
                print(e)
                return False
        else:
            return False

    
    def remove(self):
        category_remove = self.find_by_id()
        try:
            db.session.delete(category_remove)
            db.session.commit()
            return category_remove
        except Exception as e:
            print(e)
            return False
