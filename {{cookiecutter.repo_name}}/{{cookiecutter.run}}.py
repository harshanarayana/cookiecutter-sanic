from {{cookiecutter.app_name}}.{{cookiecutter.app_name}} import app
from {{cookiecutter.app_name}}.util import sanic_config_manager

sanic_config_manager(app, prefix="{{cookiecutter.sanic_env_prefix}}")


if __name__ == "__main__":
    app.run()