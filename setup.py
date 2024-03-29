"""setup tool"""
from setuptools import find_packages, setup

setup(
    name='rc-car',
    version='0.1.0',
    test_suite='test',
    packages=find_packages(include=['rc_car']),
    install_requires=[
        "behave==1.2.6",
        "pygame==2.1.2",
        "flask",
        "Flask-RESTful==0.3.9",
        "freezegun",
        "pytest-cov",
        "PyYAML",
        "requests",
        "mock"
    ],
    python_requires='>=3.6'
)
