from sanic import Sanic
from sanic.response import json
from sanic_openapi import swagger_blueprint, openapi_blueprint, doc
from {{cookiecutter.app_name}}.blueprint.health import health
{% if cookiecutter.enable_orm == 'true' -%}
from {{cookiecutter.app_name}}.model import DATABASE
from {{cookiecutter.app_name}}.blueprint.user import user
from {{cookiecutter.app_name}}.util import setup_database_creation_listener
{%- endif %}
{% if cookiecutter.enable_rate_limiter == 'true' -%}
from {{cookiecutter.app_name}}.util import setup_rate_limiter
{%- endif %}


app = Sanic(__name__)

{% if cookiecutter.enable_rate_limiter == 'true' -%}
limiter = setup_rate_limiter(app)
{%- endif %}


app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)

app.blueprint(health)

{% if cookiecutter.enable_orm == 'true' -%}
app.blueprint(user)
setup_database_creation_listener(app, DATABASE)
{%- endif %}


@app.route("/")
async def default(request):
    return json({"message": "hello Sanic!"})
