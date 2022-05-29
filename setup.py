from setuptools import setup, find_packages

setup(
    name="ipyreporter",
    version="0.0.1",
    packages=find_packages(
        where="./src",
        include="ipyreporter",
    ),
    install_requires=[
        "jinja2",
    ]
)
