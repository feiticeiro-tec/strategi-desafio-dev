from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from .hero import Hero
from .equipe import Equipe
from .connections import Connection

def init_app(app):
    db.init_app(app)