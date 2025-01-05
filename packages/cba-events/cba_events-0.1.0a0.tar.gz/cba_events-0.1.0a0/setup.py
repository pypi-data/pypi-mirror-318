from setuptools import setup, find_packages

setup(
    name="cba-events",
    version="0.1.0-alpha",
    packages=find_packages(),
    install_requires=[
        "confluent-kafka>=2.0.0",
        "dataclasses-json>=0.5.7",
    ],
    python_requires=">=3.8",
)
