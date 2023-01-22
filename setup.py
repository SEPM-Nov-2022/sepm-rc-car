"""setup tool"""
from setuptools import find_packages, setup

setup(
    name='rc-car',
    version='0.1.0',
    test_suite='test',
    packages=find_packages(exclude=['features', 'docs']),
    install_requires=[
        "behave==1.2.6",
        "pygame==2.1.2",
        "pytest-cov"
    ],
    python_requires='>=3.6'
)
