# -*- coding:utf-8 -*-
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from celery import Celery
from config import Config

db = SQLAlchemy()
mail = Mail()
cors = CORS()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)


def create_app():
    app = Flask(__name__, static_url_path='')
    app.config.from_object(Config)
    db.init_app(app)
    mail.init_app(app)
    cors.init_app(app)
    celery.conf.update(app.config)

    from main import main
    app.register_blueprint(main, url_prefix='/api/v1.0')

    from flask import render_template

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    return app
