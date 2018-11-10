{%- if cookiecutter.tox_env == "py35" -%}
FROM python:3.5-slim
{%- elif cookiecutter.tox_env == "py36" -%}
FROM python:3.6-slim
{%- elif cookiecutter.tox_env == "py37" -%}
FROM python:3.7-slim
{%- else -%}
FROM python:3.6-slim
{% endif %}
MAINTAINER {{cookiecutter.maintainer}}


# Start Installing the Basic Dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn

RUN mkdir -p /sanic/config
RUN mkdir -p /sanic/{{cookiecutter.app_name}}

COPY config/* /sanic/config/
COPY {{cookiecutter.app_name}}/ /sanic/{{cookiecutter.app_name}}/
COPY requirements.txt /sanic
COPY {{cookiecutter.run}}.py /sanic/{{cookiecutter.run}}.py
COPY .env /sanic/.env

WORKDIR /sanic
RUN find . -type f

ENV {{cookiecutter.sanic_env_prefix}}SERVER_PORT {{cookiecutter.sanic_port}}
ENV {{cookiecutter.sanic_env_prefix}}SERVER_HOST {{cookiecutter.sanic_host}}

EXPOSE {{cookiecutter.sanic_port}}

ENTRYPOINT ["gunicorn", "{{cookiecutter.run}}:app", "--config", "/sanic/config/gunicorn.conf", "--log-config", "/sanic/config/logging.conf", "-b", "{{cookiecutter.sanic_host}}:{{cookiecutter.sanic_port}}", "--worker-class",  "sanic.worker.GunicornWorker"]
