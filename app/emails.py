# -*- coding:utf-8 -*-
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + ' verify code',
                  sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template('email/verifyCode' + '.txt', **kwargs)
    msg.html = render_template('email/verifyCode' + '.html', **kwargs)
    thr_mail = Thread(target=send_async_email, args=[app, msg])
    thr_mail.start()
    return thr_mail
