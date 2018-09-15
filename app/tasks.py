# -*- coding:utf-8 -*-
from flask import current_app, render_template
from flask_mail import Message

from . import mail, celery


@celery.task
def send_email(to, code):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' verify code',
                  sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template('email/verifyCode' + '.txt', code=code)
    msg.html = render_template('email/verifyCode' + '.html', code=code)
    mail.send(msg)
