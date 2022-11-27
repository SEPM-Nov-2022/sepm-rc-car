"""setup tool"""
from setuptools import setup, find_packages

### graphviz is also required
### python-tk is also to be installed

setup(
    name='rc-car',
    version='0.1.0',
    test_suite = 'test',
    install_requires=[
        "behave==1.2.6"
    ],
    python_requires='>=3.6'
)
