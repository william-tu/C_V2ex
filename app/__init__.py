# -*- coding:utf-8 -*-
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mail.init_app(app)
    from main import main
    app.register_blueprint(main, url_prefix='/api/v1.0')

    return app
