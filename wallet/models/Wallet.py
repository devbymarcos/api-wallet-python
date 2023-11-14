from wallet.ext.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date, func, ForeignKey
from sqlalchemy.orm import relationship
from wallet.ext.database import db


class Wallet(Base):
    __tablename__ = "app_wallet"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    option_wallet = Column(Integer)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(),
                        onupdate=func.current_timestamp())

    def find_all(self, user_id):
        wallet = db.session.execute(
            db.select(Wallet).filter_by(user_id=user_id)).all()

        if wallet is not None:
            return wallet
        else:
            return None

    def find_all_reduce(self, user_id):
        result = self.find_all(user_id=user_id)
        if (result == None):
            return result

        data_result = [
            {'name': wallet[0].name, 'description': wallet[0].description} for wallet in result
        ]

        return data_result
