from setuptools import setup
from setuptools import find_packages


VERSION = '0.1.0'

setup(
    name='soit-web',  # package name
    version=VERSION,  # package version
    description='This is the Python SDK for the Soit API, which allows you to easily integrate Soit into your Python applications.',  # package description
    packages=find_packages(),
    zip_safe=False,
)