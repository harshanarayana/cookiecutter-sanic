import os
import shutil

enable_swagger = '{{cookiecutter.enable_swagger}}' == 'y'


def cleanup_requirements_file(file_name, items_to_remove):
    with open(file_name, "r") as fh:
        data = fh.read()
    os.remove(file_name)
    data = data.split("\n")
    data = [d for d in data if not d in items_to_remove]
    with open(file_name, "w") as fh:
        fh.write("\n".join(data))


if enable_swagger:
    os.rename(
        "{{cookiecutter.app_name}}/{{cookiecutter.app_name}}-swagger.py",
        "{{cookiecutter.app_name}}/{{cookiecutter.app_name}}.py")

    os.rename(
        "{{cookiecutter.app_name}}/blueprint/health/swagger-__init__.py",
        "{{cookiecutter.app_name}}/blueprint/health/__init__.py")

dependencies_to_remove = []

if not enable_swagger:
    dependencies_to_remove.append("sanic-openapi")

for req_type in ["", "-dev", "-doc"]:
    cleanup_requirements_file("requirements{}.txt".format(req_type), dependencies_to_remove)
