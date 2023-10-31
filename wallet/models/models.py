from wallet.ext.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date, func, ForeignKey
from sqlalchemy.orm import relationship
from wallet.ext.database import db


class Invoice(Base):
    __tablename__ = "app_invoice"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    wallet_id = Column(Integer, ForeignKey('app_wallet.id'))
    category_id = Column(Integer, ForeignKey('app_category.id'))
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    due_at = Column(Date)
    type = Column(String)
    pay = Column(String)
    repeat_when = Column(String)
    period = Column(String)
    group_quota = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(),
                        onupdate=func.current_timestamp())


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
