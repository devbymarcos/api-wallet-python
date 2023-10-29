from importlib import import_module
from dynaconf import FlaskDynaconf


def load_extension(app):
    for extension in app.config.get("EXTENSIONS"):
        mod = import_module(extension)
        mod.init_app(app)


def init_app(app):
    FlaskDynaconf(app)
