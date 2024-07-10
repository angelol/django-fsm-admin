#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

import fsm_admin

readme = open("README.rst").read()

setup(
    name="django-fsm-admin-2",
    version=fsm_admin.__version__,
    author=fsm_admin.__author__,
    description="Integrate django-fsm-2 state transitions into the django admin",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author_email="dev@coral.li",
    url="https://github.com/coral-li/django-fsm-admin-2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=4.2",
        "django-fsm-2>=3.0.0",
    ],
    keywords="django fsm admin",
    license="MIT",
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
