from . import Base
from sqlalchemy import Column, Integer, String


class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, id, name):
        self.name = name
        self.id = id
