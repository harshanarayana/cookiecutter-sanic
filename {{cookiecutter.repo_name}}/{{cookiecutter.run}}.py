from {{cookiecutter.app_name}}.{{cookiecutter.app_name}} import app
from {{cookiecutter.app_name}}.util import sanic_config_manager
{% if cookiecutter.run_mode == 'async_mode' %}
from asyncio import get_event_loop, ensure_future
{% endif %}
{% if cookiecutter.enable_opentracing == 'True' %}
from {{cookiecutter.app_name}}.plugin.opentracing import setup_opentracing

setup_opentracing(app=app)

{% endif %}

sanic_config_manager(app, prefix="{{cookiecutter.sanic_env_prefix}}")


if __name__ == "__main__":
{% if cookiecutter.run_mode == 'sanic_dev_mode' or cookiecutter.run_mode == 'sanic_workers' %}
    app.run(
        host="{{cookiecutter.sanic_host}}",
        port="{{cookiecutter.sanic_port}}",
        {% if cookiecutter.run_mode == 'sanic_workers' -%}worker={{cookiecutter.workers}},{%- endif %}
        {% if cookiecutter.run_mode == 'sanic_dev_mode' -%}debug=True,{%- endif %}
        {% if cookiecutter.enable_auto_reload == 'y' and cookiecutter.run_mode == 'sanic_dev_mode' -%}auto_reload=True{%- endif %}
    )
{% elif cookiecutter.run_mode == 'async_mode' %}
    server = app.create_server(
        host="{{cookiecutter.sanic_host}}",
        port="{{cookiecutter.sanic_port}}",
    )
    try:
        loop = get_event_loop()
        task = ensure_future(server)
        loop.run_forever()
    except:
        loop.stop()
{% else %}
    app.run()
{% endif %}
