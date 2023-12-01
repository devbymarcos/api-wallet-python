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

    @classmethod
    def find_by_id(cls, id):
        try:
            wallet = db.session.execute(
                db.select(Wallet).filter_by(id=id)).scalar_one()
        except Exception as e:
            print(e)
            return None

        return wallet

    @classmethod
    def remove(cls, id):
        drop_instance = cls.find_by_id(id)
        if drop_instance:
            try:
                db.session.delete(drop_instance)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback()
                print(e)
                return False
        else:
            return False
