from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


db = SQLAlchemy()
Base = declarative_base()


def init_app(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.DATABASE_URL
    db.init_app(app)
