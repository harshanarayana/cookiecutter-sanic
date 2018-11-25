# Changelog


## (unreleased)

### Other

* Feat: add release version and change log support. [Harsha Narayana]

  As part of this commit, following changes are implemented.

  1. Release version management via `bumpversion`
  2. Change log management via `gitchangelog`
  3. Documentation support for the rendered sanic application
  4. Makefile support and additional unit tests for sanic app generation

* Feat: enable multiple run modes in sanic. [Harsha Narayana]

  This commit provides a mechanism to pick multiuple run modes for running
  you sanic application. Based on the selection done by the user, the
  right setup will be generated.

  As part of this commit, necessary features required to unit test your
  application will be generated automatically.

  It also adds a few sample usecase example to show you how to employ the
  `pytest-sanic` framework to test your code.

* Feat: enable travis integration. [Harsha Narayana]

  As part of this commit, the following changes will be included.

  1. Unit Test support via `pytest-cookie`
  2. `tox` env enhancements
  3. Travis integration enhancemnt to support multiple tox versions

* Feat: add semaphoreci build badge. [Harsha Narayana]

* Feat: add github template support for PR and Issues. [Harsha Narayana]

  As part of this commit, the following changes will be enabled

  1. Github Templates
  2. Test Utility to generate sanic app during development
  3. Fix Travis Integration issues

* Feat: enable cookiecutter template support for sanic. [Harsha Narayana]

  As part of this commit the following changes will be enabled.

  1. Basic Sanic App template generation
  2. Conditional Docker Support with Gunicorn Run mode
  3. Unit Test setup using `tox`
  4. Sample health APIs via `sanic blueprints`
  5. Conditional requirements file
  6. `docker` support via `Dockerfile` and `docker-compose`

* Initial commit. [Harsha Narayana]
