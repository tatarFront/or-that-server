import asyncpg

async def connect(app): 
    connect_link = 'postgres://postgres:password@localhost:5432/or_that'
    app.config['db'] = await asyncpg.connect(connect_link)
    print('DB', app.config['db'])

async def disconnect(app): 
    app.config['db'].close()