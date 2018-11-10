from os import environ
from sanic import Sanic


def sanic_config_manager(app: Sanic, prefix: str="SANIC_"):
    for variable, value in environ.items():
        if variable.startswith(prefix):
            _, key = variable.split(prefix, 1)
            app.config[key] = value
