# -*- coding:utf-8 -*-
from flask import jsonify

from app.models import User
from app.responses import bad_request, suc_204, suc_201
from auth import basic_auth
from . import main


@main.route('/users/<int:id>/followed', methods=['GET'])
@basic_auth.login_required
def get_user_followed(id):
    user = User.query.get_or_404(id)
    return jsonify({f.followed.to_json() for f in user.followed.all()})


@main.route('/users/<int:id>/followers', methods=['GET'])
@basic_auth.login_required
def get_user_followers(id):
    user = User.query.get_or_404(id)
    return jsonify({f.follower.to_json() for f in user.followers.all()})


@main.route('/users/<int:p_id>/follow/users/<int:b_id>', methods=['POST'])
@basic_auth.login_required
def add_follow_user(p_id, b_id):
    if p_id == b_id:
        return bad_request('user can not  follow themselves')
    user1 = User.query.get_or_404(p_id)
    user2 = User.query.get_or_404(b_id)
    user1.follow(user2)
    return suc_201('cancel follow successfully')


@main.route('/users/<int:p_id>/follow/users/<int:b_id>', methods=['DELETE'])
@basic_auth.login_required
def delete_follow_user(p_id, b_id):
    if p_id == b_id:
        return bad_request('user can not cancel follow themselves')
    user1 = User.query.get_or_404(p_id)
    user2 = User.query.get_or_404(b_id)
    user1.unfollow(user2)
    return suc_204('cancel follow successfully')
