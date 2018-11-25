#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


with open(path.join(path.dirname(path.abspath(__file__)), "requirements.txt")) as requirement_file:
    requirements = requirement_file.read().split("/n")

setup_requirements = ["pytest-runner"]

with open(path.join(path.dirname(path.abspath(__file__)), "requirements-dev.txt")) as dev_requirement_file:
    test_requirements = dev_requirement_file.read().split("/n")


{%- set python_environments = {
    'py35': "Programming Language :: Python :: 3.5",
    'py36': "Programming Language :: Python :: 3.6",
    'py37': "Programming Language :: Python :: 3.7"
} %}

setup(
    author="{{ cookiecutter.maintainer.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
{%- if cookiecutter.tox_env in python_environments %}
        '{{ python_environments[cookiecutter.tox_env] }}',
{%- endif %}
    ],
    description="{{ cookiecutter.app_name }}",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords="{{ cookiecutter.app_name }}",
    name="{{ cookiecutter.app_name }}",
    packages=find_packages(include=['{{ cookiecutter.app_name }}']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False
)
