from os import environ
from sanic import Sanic
{% if cookiecutter.enable_orm == 'true' -%}
from gino.ext.sanic import Gino
{%- endif %}
{% if cookiecutter.enable_rate_limiter == 'true' -%}
from sanic_limiter import Limiter, get_remote_address
{%- endif %}

def sanic_config_manager(app: Sanic, prefix: str = "SANIC_"):
    for variable, value in environ.items():
        if variable.startswith(prefix):
            _, key = variable.split(prefix, 1)
            app.config[key] = value


{% if cookiecutter.enable_orm == 'true' -%}
def setup_database_creation_listener(app: Sanic, database: Gino):
    database.init_app(app)
    @app.listener("after_server_start")
    async def setup_database(app: Sanic, loop):
        await database.gino.create_all()
{%- endif %}


{% if cookiecutter.enable_rate_limiter == 'true' -%}
def setup_rate_limiter(app: Sanic):
    limiter = Limiter(
        app,
        global_limits=[
            "10/hour",
            "1/second"
        ],
        key_func=get_remote_address,
        strategy='moving-window',
        storage_uri="memory://")

    return limiter
{%- endif %}

