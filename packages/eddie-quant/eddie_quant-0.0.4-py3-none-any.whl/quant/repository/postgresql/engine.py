import os

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, Session


class Engine(object):
    def __init__(self):
        db_url = os.environ['DATABASE_URL']

        self.__engine = db.create_engine(db_url)
        self.__Session = sessionmaker(bind=self.__engine)

    def session(self) -> Session:
        return self.__Session()
