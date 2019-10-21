from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from repository.base import Base
from repository.user import User


from services.status import status_bp
from setup import setup_app
# from db_connect import connect, disconnect
CONNECT_LINK='postgres://postgres:password@localhost:5432/or_that'

app=Sanic('or_that')
app.config.from_pyfile('./.env')

# connect to db
@app.listener('after_server_start')
async def connect_db(app, loop): 
    app.config['base']=await Base.create(connect_link=CONNECT_LINK)
    app.config['user']=await User.create(connect_link=None, connecting=app.config['base'].db)
    app.config['user'].get(_id='123')
    # await app.config['base'].create(connect_link=CONNECT_LINK)
    
@app.listener('after_server_stop')
async def disconnect_db(app, loop): 
    await app.config['base'].disconnect()
# init services
setup_app(app)

if __name__ == "__main__":
    app.run(
        host=app.config.get('HOST', '0.0.0.0'), 
        port=app.config.get('PORT', 8000), 
        debug=app.config.get('DEBUG', True), 
        access_log=app.config.get('access_log', True)
    )