import asyncpg

class Base(object):
    def __init__(self):
        self.db = None

    # for use async when class created
    @classmethod
    async def create(cls, connect_link, **kwargs):
        self = cls()
        
        if(kwargs.get('connecting') != None):
            cls.db = connect(connect_link, **kwargs)
        
        return self

    async def connect(connect_link): 
        return await asyncpg.connect(connect_link)

    async def disconnect(self): 
        self.db.close()