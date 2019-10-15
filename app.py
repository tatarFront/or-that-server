from sanic import Sanic
from sanic.log import logger #логи
from sanic.response import json #запросы

from services.status import status_bp
from setup import setup_app

app = Sanic('or_that')
app.config.from_pyfile('./.env')

@app.route('/')
async def test(req):
    logger.info('this is log')
    return json({"hi": 'world'})

setup_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, access_log=True)