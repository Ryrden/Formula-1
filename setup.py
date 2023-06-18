#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="proj-labbd",
    version="0.1.0",
    install_requires=requirements,
    packages=find_packages(include=["proj_labbd"]),
    entry_points={"console_scripts": ["proj_labbd=proj_labbd.__main__:main"]},
)
