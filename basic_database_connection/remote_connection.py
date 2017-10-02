from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from . import DatabaseLocalConnection

class DatabaseRemoteConnection(DatabaseLocalConnection):
    def __init__(self, config, tunnel):
        self.tunnel = tunnel
        self.config = config

    def start(self):
        if 'keyfile' in self.tunnel:
            self.server = SSHTunnelForwarder(
                ssh_address=(self.tunnel['host'], self.tunnel['port']),
                ssh_username=self.tunnel['user'],
                ssh_pkey=self.tunnel['keyfile'],
                remote_bind_address=(self.tunnel['remote'], self.tunnel['remote_port']))
        else:
            self.server = SSHTunnelForwarder(
                ssh_address=(self.tunnel['host'], self.tunnel['port']),
                ssh_username=self.tunnel['user'],
                ssh_password=self.tunnel['password'],
                remote_bind_address=(self.tunnel['remote'], self.tunnel['remote_port']))

        # Start server tunnel connection
        self.server.start()

        local_port = str(self.server.local_bind_port)
        self.config['port'] = local_port
        
        super(DatabaseRemoteConnection, self).start()

    def stop(self):
        super(DatabaseRemoteConnection, self).stop()
        self.server.stop()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()
