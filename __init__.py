from flask import Flask

from app.vistas.ingredientes import ingredientes_bp
from conf.config import DevelpmentConfig

ACTIVE_ENDPOINTS = [
    ('/ingredientes',ingredientes_bp),
]

def create_app(config=DevelpmentConfig):
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config.from_object(config)
    
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    return app

if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()