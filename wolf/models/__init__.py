import sqlalchemy as db
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine(
    'postgresql://hasstrupezekiel@localhost:5432/wolf_development')
engine.connect()

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()
