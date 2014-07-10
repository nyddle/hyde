# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import hyde
version = hyde.__version__

setup(
    name='hyde',
    version=version,
    author='',
    author_email='nyddle@gmail.com',
    packages=[
        'hyde',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['hyde/manage.py'],
)