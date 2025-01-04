from setuptools import setup, find_packages
import io

setup(
    name="pyafplus",
    version="0.1.4",
    author="dhjs0000",
    description="A collection of Python utility functions and extensions",
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dhjs0000/PyPlus",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 