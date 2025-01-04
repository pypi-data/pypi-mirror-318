import os

from setuptools import setup, find_packages

setup(
    name="identt",
    version=os.getenv("PACKAGE_VERSION", "0.1.0"),
    packages=find_packages(where="."),
    package_dir={"": "."},
    install_requires=["requests"],
    author="brdge.ai",
    description="Python SDK for Iden API interactions",
)
