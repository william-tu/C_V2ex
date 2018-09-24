# -*- coding:utf-8 -*-
from flask import g, request, jsonify

from app.decorates import json_params_required, user_own_required
from app.models import User, Post, Article
from app.responses import suc_201, suc_200, pagination_response
from auth import basic_auth
from . import main


@main.route('/users/<int:id>/permissions', methods=['GET'])
@basic_auth.login_required
def get_user_permissions(id):
    user = User.query.get_or_404(id)
    return jsonify(user.role.permissions)


@main.route('/current-user/info', methods=['GET', 'PUT'])
@basic_auth.login_required
@json_params_required([{'methods': ['PUT'], 'field': 'avatar', 'required': False}])
def current_user():
    if request.method == 'GET':
        return jsonify(g.current_user.to_json())
    elif request.method == 'PUT':
        print g.current_user
        g.current_user.from_json(request.json)
        return suc_201('update successfully')


@main.route('/users/<int:id>/info', methods=['GET'])
def get_user(id):
    u = User.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(u.to_json())


@main.route('/users/<int:id>/info', methods=['PUT'])
@basic_auth.login_required
@user_own_required(methods=['PUT'], user_id_key='id')
def put_user(id):
    u = User.query.get_or_404(id)
    u.from_json(request.json)
    return suc_201('update successfully')


@main.route('/users/<int:user_id>/favor/posts/<int:post_id>', methods=['GET', 'POST', 'DELETE'])
@basic_auth.login_required
def favor_posts(user_id, post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    if request.method == 'GET':
        return jsonify({'favor': user.has_favored_post(post)})
    elif request.method == 'POST':
        user.favor_post(post)
        return suc_200('OK')
    elif request.method == 'DELETE':
        user.cancel_favor_post(post)
        return suc_200('OK')


@main.route('/users/<int:id>/favor/posts', methods=['GET'])
def get_user_favor_posts(id):
    user = User.query.get_or_404(id)
    return pagination_response(user.favor_posts)


@main.route('/users/<int:user_id>/favor/articles/<int:article_id>', methods=['GET', 'POST', 'DELETE'])
@basic_auth.login_required
def favor_articles(user_id, article_id):
    user = User.query.get_or_404(user_id)
    article = Article.query.get_or_404(article_id)
    if request.method == 'GET':
        return jsonify({'favor': user.has_favored_article(article)})
    elif request.method == 'POST':
        user.favor_article(article)
        return suc_200('OK')
    elif request.method == 'DELETE':
        user.cancel_favor_article(article)
        return suc_200('OK')


@main.route('/users/<int:id>/favor/articles', methods=['GET'])
@basic_auth.login_required
def get_user_favor_articles(id):
    user = User.query.get_or_404(id)
    return pagination_response(user.favor_articles)
