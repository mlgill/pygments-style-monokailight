#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1'
long_description = '\n'.join([
    open('README.rst').read(),
    ])

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='pygments-style-monokailight',
    version=version,
    description='Pygments version of the monokai theme for light backgorunds.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['pygments', 'style', 'monokai', 'syntax highlighting'],
    author='Michelle Gill',
    author_email='michelle@michellelynngill.com',
    url='https://github.com/mlgill/pygments-style-monokailight',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        monokailight=pygments_style_monokailight:MonokaiLightStyle
    """,
    zip_safe=False,
)
