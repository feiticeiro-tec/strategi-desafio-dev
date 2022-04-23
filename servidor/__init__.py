from flask import Flask
from servidor import database
import json

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.config.from_file('app_config.json',json.load)
    with app.app_context():
        database.init_app(app)
        from servidor import routes
    return app