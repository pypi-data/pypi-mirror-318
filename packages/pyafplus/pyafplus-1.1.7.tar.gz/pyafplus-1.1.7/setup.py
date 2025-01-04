from setuptools import setup, find_packages

setup(
    name="pyafplus",
    version="1.1.7",
    author="dhjs0000",
    author_email="dhjsllll@foxmail.com",
    description="Python Advanced Features Plus - 提供多种实用的 Python 扩展功能",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dhjs0000/PyPlus",
    packages=find_packages(),
    package_data={
        'progressplus': ['*.pyd'],  # 包含编译好的 Rust 扩展
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Rust",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    keywords=[
        "python",
        "utility",
        "progress bar",
        "rust extension",
        "high performance",
        "string math",
        "big number",
        "data structures"
    ]
) 