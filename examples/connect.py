#!/bin/env/python
import os
from envparse import env

from basic_database_connection.connection import get_connection

if __name__ == '__main__':
    '''connect
    A basic example of usage "basic_database_connection".

    Usage:
    python connect.py
    '''

    # Load enviroment parameters from .env file
    env.read_envfile('.env')

    # Prepare database connection
    database = {
        'driver': env('DB_DRIVER'),
        'user': env('DB_USER'),
        'password': env('DB_PASSWORD'),
        'host': env('DB_HOST'),
        'port': env('DB_PORT'),
        'database': env('DB_NAME'),
    }

    # Prepare tunneling connection
    tunnel = None
    if env('DB_TUNNELING', cast=bool, default=False):
        tunnel = {
            'host': env('DB_TUNNEL_HOST'),
            'port': env('DB_TUNNEL_PORT', cast=int),
            'user': env('DB_TUNNEL_USER'),
            'password': env('DB_TUNNEL_PASSWORD'),
            'remote': env('DB_TUNNEL_REMOTE'),
            'remote_port': env('DB_TUNNEL_REMOTE_PORT', cast=int),
        }

    with get_connection(database, tunnel) as conn:
        results = conn.query_execute('SELECT * FROM app_catalog')

        for row in results:
            print(row)
