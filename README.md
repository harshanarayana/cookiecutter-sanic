# Cookiecutter Sanic Package

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for Sanic Applications


# Feature
 
* Swagger support via [sanic-openapi](https://github.com/huge-success/sanic-openapi)
* `Docker` and `docker-compose` Support
* `Gunicorn` App runner setup
* Conditional requirements.txt management
* JSON logging for `Docker` containers
* Wrapper for `sanic` App Configuration via environment variable prefix
* Default `health` and `status` API blueprints
* `tox` Environment Setup with `py35`, `py36` `py37`
* Unit testing via `pytest` and `pytest-sanic`


# Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/harshanarayana/cookiecutter-sanic.git
```