from sanic.blueprints import Blueprint
from sanic.response import json

health = Blueprint("health", url_prefix="/health")
health_swagger = Blueprint("health", url_prefix="/health")


@health.route("/status")
async def health_status(request):
    return json({"status": "OK"})
