from setuptools import setup, find_packages

setup(
    name="Metdley",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Metdley",
    author_email="contact@metdley.com",
    description="A Python client for the Metdley API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://metdley.com",
)
