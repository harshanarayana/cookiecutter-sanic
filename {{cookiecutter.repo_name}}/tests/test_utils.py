from os import environ
from sanic import Sanic
from {{cookiecutter.app_name}}.util import sanic_config_manager
from pytest import raises

def test_app_config_default_env_prefix(sanic_app: Sanic):
    environ["SANIC_PARAM1"] = "value1"
    environ["SANIC_PARAM2"] = "p2"
    environ["NON_SANIC_PARAM3"] = "p3"
    sanic_config_manager(app=sanic_app)
    assert sanic_app.config["PARAM1"] == "value1"
    assert sanic_app.config["PARAM2"] == "p2"
    with raises(expected_exception=KeyError) as e:
        _ = sanic_app.config["PARAM3"]


def test_app_config_custom_env_prefix(sanic_app: Sanic):
    environ["NON_SANIC_PARAM3"] = "p3"
    sanic_config_manager(app=sanic_app, prefix="NON_SANIC_")
    assert sanic_app.config["PARAM3"] == "p3"
