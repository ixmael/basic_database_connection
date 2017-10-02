from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DatabaseLocalConnection(object):
    def __init__(self, config):
        self.config = config

    def start(self):
        engine = create_engine('{driver}://{user}:{password}@{host}:{port}/{database}'
            .format(**self.config))

        Session = sessionmaker(bind=engine, autocommit=True)
        self.session = Session()

    def get_session(self):
        return self.session

    def stop(self):
        if self.session:
            self.session.close()

    def query_execute(self, query):
        result = None
        try:
           result = self.session.execute(query)
        except Exception as e:
            raise e

        return result

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()
