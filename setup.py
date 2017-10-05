# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="IronMud",
    version="0.0.1",
    author="Janusz Janowski",
    author_email="januszjanowski@outlook.com",
    description=("Simple game in console"),
    license="MIT",
    keywords="iron mud console game",
    url="https://github.com/esentino/IronMud",
    packages=['tests'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console"
    ]
)
