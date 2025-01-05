from setuptools import setup, find_packages

setup(
    name="rover_connect2_module",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["sim800l-gsm-module"],
)
