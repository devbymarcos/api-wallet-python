from flask import Flask
from wallet.ext import configuration
from wallet.ext import database


app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)


# aqui vai as rotaflass


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
