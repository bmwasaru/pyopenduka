from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
requirements = [str(req.req) for req in install_reqs]

setup(
    name='pyopenduka',
    version='1.0',
    description='The Open Duka library for python',
    packages=find_packages(exclude=['test']),
    install_requires=requirements,
    keywords='open duka library'
)