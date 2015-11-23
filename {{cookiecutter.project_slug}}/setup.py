#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from setuptools import find_packages

import os
import re
import codecs
def read_version():
    version_file = codecs.open(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                '{{ cookiecutter.project_slug }}/__init__.py'),
            'r', 'utf-8' ).read()
    return re.search( r"^__version__ = ['\"]([^'\"]*)['\"]",
            version_file, re.M ).group(1)

version = read_version()

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(exclude=[ "docs", "tests*" ]),
    package_dir={'{{ cookiecutter.project_slug }}':
                 '{{ cookiecutter.project_slug }}'},
    include_package_data=True,
    license='Apache 2.0',
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=requirements,
    tests_require=test_requirements
    zip_safe=False,
)




