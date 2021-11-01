from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

e = create_engine('sqlite:///first.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=e))
Base = declarative_base()
Base.query = db_session.query_property()


def init():
    Base.metadata.create_all(bind=e)
