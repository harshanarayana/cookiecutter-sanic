from sys import path as sys_path
from os import path as os_path
sys_path.insert(0, os_path.join(os_path.dirname(os_path.abspath(__file__)), ".."))
from pytest import fixture
from {{cookiecutter.app_name}} import app
import logging


@fixture
def sanic_app(request):
    return app


@fixture
def sanic_tester(loop, sanic_app, test_client):
    return loop.run_until_complete(test_client(sanic_app))


@fixture
def logger():
    logger = logging.getLogger(__name__)
    numeric_level = getattr(logging, "DEBUG", None)
    logger.setLevel(numeric_level)
    return logger
