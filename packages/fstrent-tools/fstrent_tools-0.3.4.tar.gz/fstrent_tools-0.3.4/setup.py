# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="fstrent_tools",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
) 