from flask import Flask, request
from app.database.db import db



def create_app():
    app = Flask(__name__)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app