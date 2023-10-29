from flask import Flask
from wallet.ext import configuration


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extension(app)
    return app

    # if __name__ == '__main__':
    #     app.run(port=5000, host="0.0.0.0", debug=True)
