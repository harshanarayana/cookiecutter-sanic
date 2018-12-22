{% if cookiecutter.enable_orm == 'true' -%}
from gino.ext.sanic import Gino


DATABASE = Gino()
{%- endif -%}
