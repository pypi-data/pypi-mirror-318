# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="fstrent_tools",
    version="0.3.4",
    packages=find_packages(where="src"),
    package_dir={"fstrent_tools": "src"},
    include_package_data=True,
    author="FSTrent",
    author_email="wrmartel3@gmail.com",
    description="Tools for Python Development",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wrm3/fstrent_tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 