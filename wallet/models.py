from wallet.ext.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func


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
