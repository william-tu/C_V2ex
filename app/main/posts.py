# -*- coding:utf-8 -*-
from flask import jsonify, request, g, current_app, url_for

from app.decorates import json_field_acceptable, permission_required
from app.models import Post, User, Permission
from app.responses import suc_204
from auth import basic_auth
from . import main


@main.route('/users/<int:id>/posts', methods=['GET'])
@basic_auth.login_required
def get_user_posts(id):
    user = User.query.get_or_404(id)
    return jsonify([p.to_json() for p in user.posts])


@main.route('/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.paginate(page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('main.get_posts', page=page - 1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('main.get_posts', page=page + 1, _external=True)
    return jsonify({'data': [post.to_json() for post in posts], 'prev': prev, 'next': next, 'pages': pagination.pages,
                    'count': pagination.total})


@main.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())


@main.route('/posts/<int:id>', methods=['DELETE'])
@basic_auth.login_required
@permission_required(Permission.MODERATE_ARTICLES_COMMENTS)
def delete_post(id):
    post = Post.query.get_or_404(id)
    post.delete()
    return suc_204('delete post successfully')


@main.route('/posts', methods=['POST'])
@basic_auth.login_required
@json_field_acceptable(['body'])
@permission_required(Permission.WRITE_ARTICLES)
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    post.save()
    return jsonify(post.to_json())
