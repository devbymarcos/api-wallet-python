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
    
    def __init__(
        self,
        id=None,
        user_id=None,
        name=None,
        description=None,
        option_wallet=None):
        
        self.id=id
        self.user_id=user_id
        self.name = name
        self.description = description
        self.option_wallet=option_wallet


    
    def find_all(self):
        wallet = db.session.execute(
            db.select(Wallet).filter_by(user_id=self.user_id)).all()

        if wallet is not None:
            return wallet
        else:
            return None

    
    def find_by_id(self):
        try:
            wallet = db.session.execute(
                db.select(Wallet).filter_by(id=self.id)).scalar_one()
            return wallet
        except Exception as e:
            print(e)
            return None

        

   
    def remove(self):
        drop_instance = self.find_by_id(self.id)
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

    
    def save(self):
        wallet = Wallet(
                user_id=self.user_id,
                name=self.name,
                description=self.description,
                option_wallet=self.option_wallet
            )
        try:
            db.session.add(wallet)
            db.session.commit()
            return wallet
        except Exception as e:
            print(e)
            return False
        


    def update(self):
        update = self.find_by_id(self.id)

        update.name = self.name
        update.description = self.description
        update.option_wallet = self.option_wallet 

        try:
            db.session.commit()
            return update
        except Exception as e:
            print(e)
            return False