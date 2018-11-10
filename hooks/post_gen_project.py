import os
import shutil

enable_swagger = '{{cookiecutter.enable_swagger}}' == 'y'

if enable_swagger:
    os.rename(
        "{{cookiecutter.app_name}}/{{cookiecutter.app_name}}-swagger.py",
        "{{cookiecutter.app_name}}/{{cookiecutter.app_name}}.py")

    os.rename(
        "{{cookiecutter.app_name}}/blueprint/health/swagger-__init__.py",
        "{{cookiecutter.app_name}}/blueprint/health/__init__.py")
