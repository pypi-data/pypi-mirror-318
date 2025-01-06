import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, Session


class Engine(object):
    def __init__(self):
        # db_url = os.environ['DATABASE_URL']
        db_url = "postgresql://postgres:omv8964@192.168.0.94/securities"

        self.__engine = db.create_engine(db_url)
        self.__Session = sessionmaker(bind=self.__engine)

    def session(self) -> Session:
        return self.__Session()
