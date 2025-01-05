# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import TYPE_CHECKING

from setuptools import setup, find_packages

if TYPE_CHECKING:
    pass

setup(
    name="TheSeedCore",
    version="0.1.8",
    packages=find_packages(),
    install_requires=[],
    author='疾风Kirito',
    author_email='1453882193@qq.com',
    description='TheSeedCore is a comprehensive modular framework designed to meet the diverse needs of modern application development. '
                'Whether building high-performance, scalable applications or integrating complex systems, '
                'TheSeedCore provides a strong foundation covering a wide range of functions. With its modular, secure and flexible design, '
                'TheSeedCore can help developers create reliable and easy-to-maintain solutions.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JFkirito/TheSeedCore',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.11,<3.12',
)
