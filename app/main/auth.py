# -*- coding:utf-8 -*-
import random

from flask import g, jsonify, request
from flask_httpauth import HTTPBasicAuth

from app.decorates import json_field_acceptable
from app.emails import send_email
from app.models import User, Permission
from app.pipelines import RedisPipeline
from app.responses import unauthorized, suc_202, suc_200
from . import main

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(email_or_token, code):
    if not email_or_token:
        return False
    if not code:
        g.current_user = User.verify_token(email_or_token)
        return g.current_user is not None
    print email_or_token, code
    if RedisPipeline().get_verify_code(email_or_token) != code:
        return False
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        user = User(email=email_or_token)
        user.save()
    g.current_user = user
    return True


@basic_auth.error_handler
def auth_error():
    return unauthorized('unauthorized error')


@main.route('/token', methods=['GET'])
@basic_auth.login_required
def token():
    user = g.current_user
    return jsonify({'token': user.generate_token(
        expiration=3600), 'expiration': 3600})


@main.route('/verifyCode', methods=['POST'])
@json_field_acceptable(['email'])
def verify_code():
    em = request.json.get('email')
    code = random.randrange(1000, 9999)
    send_email(em, code=code)
    RedisPipeline().set_verify_code(em, code)
    return suc_202('send email successfully')


@main.route('/permissions', methods=['GET'])
@basic_auth.login_required
def get_permissions():
    return jsonify(Permission.to_json())


@main.route('/check-auth')
@basic_auth.login_required
def check_auth():
    return suc_200('ok')
