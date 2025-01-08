import logging
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.config import Config

# Config
config = Config()

# Logger
# logging.getLogger('werkzeug').setLevel(logging.ERROR)


def create_app():
    from app.hooks import register_hooks
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(catch_all_404s=True)

    # Enable CORS for all domains on all routes
    CORS(app, supports_credentials=True)

    register_hooks(app, api)
    register_routes(api)

    api.init_app(app)

    return app
