from setuptools import setup, find_packages

setup(
    name="pyafplus",
    version="1.1.6",
    packages=find_packages(),
    install_requires=[],
    author="dhjs0000",
    author_email="dhjsllll@foxmail.com",
    description="Python 工具集合，提供了多种实用的扩展功能",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dhjs0000/PyPlus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 