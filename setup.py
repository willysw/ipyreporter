from setuptools import setup, find_packages

setup(
    name="ipyreporter",
    version="0.0.1",
    packages=["ipyreporter"],
    package_dir={"": "src"},
    install_requires=[
        "jinja2",
    ]
)
