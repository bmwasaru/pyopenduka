import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='openduka',
    version='0.1',
    description='Python library for the OpenDuka platform',
    packages=find_packages(exclude=['test']),
    install_requires=required,
    keywords='open duka library'
)
