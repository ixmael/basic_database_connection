from . import DatabaseLocalConnection
from . import DatabaseRemoteConnection

__version__ = '0.0.1'

def get_connection(config, tunnel=None):
    database_connection = None

    if tunnel:
        database_connection = DatabaseRemoteConnection(config, tunnel)
    else:
        database_connection = DatabaseLocalConnection(config)

    return database_connection
