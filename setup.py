# setup.py
from setuptools import setup, find_packages

setup(
    name="Flask-Deta",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "deta",
    ],
)
