# -*- coding:utf-8 -*-
from flask import jsonify, request, current_app, url_for

from app.decorates import permission_required
from app.models import Comments, User, Post, Permission
from app.pagination import Paginate
from app.responses import suc_204
from auth import basic_auth
from . import main


@main.route('/users/<int:id>/comments', methods=['GET'])
def get_user_comments(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    comments = user.comments.all()
    pagination = Paginate(comments, current_page=page, per_page=current_app.config['POSTS_PER_PAGE'])
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_comments', page=page - 1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_comments', page=page + 1, _external=True)
    return jsonify(
        {'data': [comment.to_json() for comment in comments], 'prev': prev, 'next': next, 'pages': pagination.pages,
         'count': pagination.total})


@main.route('/comments', methods=['GET'])
def get_comments():
    page = request.args.get('page', 1, type=int)
    pagination = Comments.query.paginate(page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    comments = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('main.get_comments', page=page - 1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('main.get_comments', page=page + 1, _external=True)
    return jsonify(
        {'data': [comment.to_json() for comment in comments], 'prev': prev, 'next': next, 'pages': pagination.pages,
         'count': pagination.pages})


@main.route('/posts/<int:id>/comments', methods=['GET'])
def get_post_comments(id):
    post = Post.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    comments = post.comments.all()
    pagination = Paginate(comments, current_page=page, per_page=current_app.config['POSTS_PER_PAGE'])
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_comments', page=page - 1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_comments', page=page + 1, _external=True)
    return jsonify(
        {'data': [comment.to_json() for comment in comments], 'prev': prev, 'next': next, 'pages': pagination.pages,
         'count': pagination.total})


@main.route('/comments/<int:id>', methods=['DELETE'])
@basic_auth.login_required
@permission_required(Permission.MODERATE_ARTICLES_COMMENTS)
def delete_comment(id):
    comment = Comments.query.get_or_404(id)
    comment.delete()
    return suc_204('delete comment successfully')
