# Cookiecutter Sanic Package
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fharshanarayana%2Fcookiecutter-sanic.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fharshanarayana%2Fcookiecutter-sanic?ref=badge_shield)
[![Build Status](https://semaphoreci.com/api/v1/harshanarayana/cookiecutter-sanic/branches/master/badge.svg)](https://semaphoreci.com/harshanarayana/cookiecutter-sanic)

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
* CI support for `travis`
* Github Issue and PR templates

# Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/harshanarayana/cookiecutter-sanic.git
```

# To Do

- [ ] Authentication Support (JWT, Basic Auth)
- [ ] Rate Limiter
- [ ] Caching Support via Redis/memcached
- [ ] ORM/Database Integration
- [ ] Automated Release Management
- [ ] Automated Change Log Generator


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fharshanarayana%2Fcookiecutter-sanic.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fharshanarayana%2Fcookiecutter-sanic?ref=badge_large)