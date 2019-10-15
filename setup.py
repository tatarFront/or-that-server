from sanic import Sanic

# services
from services.status import status_bp

def setup_app(app):
    app.blueprint(status_bp)