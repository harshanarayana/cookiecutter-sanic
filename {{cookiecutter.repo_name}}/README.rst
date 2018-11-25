{% for _ in cookiecutter.repo_name %}={% endfor %}
{{ cookiecutter.repo_name }}
{% for _ in cookiecutter.repo_name %}={% endfor %}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.repo_name | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
     :alt: Updates

* Documentation: https://{{ cookiecutter.repo_name | replace("_", "-") }}.readthedocs.io.

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `harshanarayana/cookiecutter-sanic`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`harshanarayana/cookiecutter-sanic`: https://github.com/harshanarayana/cookiecutter-sanic


This project enables automated version management using bumpversion_ and gitchangelog_ projects.

.. _bumpversion: https://github.com/peritus/bumpversion
.. _gitchangelog: https://github.com/vaab/gitchangelog

