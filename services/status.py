from sanic import Sanic
from sanic import Blueprint
from sanic.response import json

status_bp = Blueprint('status')

@status_bp.get('/status')
async def status(req):
    return json({ "status": "OK", "code": 200 })