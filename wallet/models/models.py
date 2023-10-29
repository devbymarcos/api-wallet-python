from wallet.ext.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date, func


class Users(Base):
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


class Wallet(Base):
    __tablename__ = "app_wallet"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    option_wallet = Column(Integer)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(),
                        onupdate=func.current_timestamp())


class Invoice(Base):
    __tablename__ = "app_invoice"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    wallet_id = Column(Integer)
    category_id = Column(Integer)
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
    user_id = Column(Integer)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(),
                        onupdate=func.current_timestamp())
