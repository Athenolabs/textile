# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='textile',
    version=version,
    description='Managing in out of fabrics',
    author='pitambar',
    author_email='pitambar.hatwar@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
