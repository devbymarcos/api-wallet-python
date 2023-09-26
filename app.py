from flask import Flask, Response, request
from database import db
from routes.user_routes import user_bp
from dotenv import load_dotenv
import os

load_dotenv()

database_uri = os.environ.get('DATABASE_URL')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db.init_app(app)


# aqui vai as rotas
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
