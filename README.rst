This is a basic database connection.
==========
The aim of this package is provide a remote or local database connection.

Installing
-------------
Manually:
::
    $ pip install git+https://github.com/ixmael/basic_database_connection
    OR
    $ git clone https://github.com/ixmael/basic_database_connection && cd envparse
    $ python setup.py install

This package use `SQLAlchemy <http://www.sqlalchemy.org/>`_ y
`SSHTunnel <https://pypi.python.org/pypi/sshtunnel>`_. The SSHTunnel require
`Paramiko <http://www.paramiko.org/>`_ and maybe install system packages
to install it.

::
    $ apt-get install build-essential libssl-dev libffi-dev python3-dev
    OR
    $ sudo yum install gcc libffi-devel python-devel openssl-devel
    OR
    $ pip install cryptography

Usage
-------------
In the dir **examples** exists a basic usage of basic_database_connection.
