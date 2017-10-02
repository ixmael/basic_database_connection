from __future__ import print_function
from setuptools import setup, find_packages

import os
import codecs
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    
    raise RuntimeError("Unable to find version string.")

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='basic_database_connection',
    version=find_version('.', 'basic_database_connection', 'connection.py'),
    description='A basic database connection',
    long_description=long_description,
    url='https://github.com/ixmael/basic_database_connection',
    author='Ismael Ramos Merlos',
    author_email='iramosmerlos@outlook.com',
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'Topic :: Software Development',
        'Topic :: Utilities',
        "Topic :: Database :: Front-Ends",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='database development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'SQLAlchemy',
        'sshtunnel',
        ],
)
