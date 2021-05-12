from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy import desc, MetaData
from models import *
from config import *
import logging

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app, resources=r"/api/*")
    
    app.logger.info("Flask app name")
    app.logger.info(__name__)
    app.config['FLASK_ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    logging.basicConfig(level=logging.DEBUG)
    app.logger.info("Starting Flask App")

    db.init_app(app)
    migrate.init_app(app, db)

    return app