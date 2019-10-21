import asyncpg

from repository.base import Base

class User(Base):

    def get(self, _id): 
        print(_id)