# -*- coding:utf-8 -*-
from flask import g, request, jsonify

from app.decorates import json_field_acceptable
from app.models import User
from app.responses import suc_201
from auth import basic_auth
from . import main


@main.route('/current-user/info', methods=['GET', 'PUT'])
@basic_auth.login_required
@json_field_acceptable(['username'], ['PUT'])
def current_user():
    if request.method == 'GET':
        return jsonify(g.current_user.to_json())
    elif request.method == 'PUT':
        g.current_user.from_json(request.json)
        return suc_201('update successfully')


@main.route('/users/<int:id>/info', methods=['GET', 'PUT'])
@basic_auth.login_required
@json_field_acceptable(['username'], ['PUT'])
def user():
    u = User.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(u.to_json())
    elif request.method == 'PUT':
        u.from_json(request.json)
        return suc_201('update successfully')
