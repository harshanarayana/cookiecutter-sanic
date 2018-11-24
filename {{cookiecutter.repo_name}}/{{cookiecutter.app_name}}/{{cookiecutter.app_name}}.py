from sanic import Sanic
from sanic.response import json
from {{cookiecutter.app_name}}.blueprint.health import health

app = Sanic(__name__)

app.blueprint(health)


@app.route("/")
async def default(request):
    return json({"message": "hello Sanic!"})
