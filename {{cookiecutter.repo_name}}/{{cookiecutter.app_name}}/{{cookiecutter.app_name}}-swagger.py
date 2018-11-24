from sanic import Sanic
from sanic.response import json
from sanic_openapi import swagger_blueprint, openapi_blueprint, doc
from {{cookiecutter.app_name}}.blueprint.health import health


app = Sanic(__name__)

app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)

app.blueprint(health)


@app.route("/")
async def default(request):
    return json({"message": "hello Sanic!"})
