#!/usr/bin/python

from setuptools import setup

setup(
    name = "python-sentry",
    version = "1.0",
    author = "Josip Domsic",
    author_email = "josip.domsic+github@gmail.com",
    description = ("Pure Python CLI for sentry, as well as client library"),
    license = "MIT",
    keywords = "python Sentry CLI",
    url = "https://github.com/ulicar/sentry-cli",
    packages=['sentry'],
    data_files = [
        ('/usr/local/bin/', [
            'sentry-cli'
        ])
    ],
)
