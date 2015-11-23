cookiecutter-dce
======================

.. image:: https://img.shields.io/travis/audreyr/cookiecutter-pypackage.svg
   :target: https://travis-ci.org/audreyr/cookiecutter-pypackage

cookiecutter template for a DCE Python package. See https://github.com/audreyr/cookiecutter.
Based on https://github.com/audreyr/cookiecutter-pypackage

generates a python project with
* Free software: Apache 2.0 license
* Vanilla testing setup with `unittest` and `python setup.py test`
* Tox_ testing: Setup to easily test for Python 2.6, 2.7
* setup.py with setuptools.find_packages() and version from package/__init__.py
  (as jay [jay_luker at harvard dot dce] had in pyhorn
  https://github.com/harvard-dce/pyhorn)


Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/harvard-dce/cookiecutter-dce.git

---
