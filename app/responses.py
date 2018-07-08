# -*- coding:utf-8 -*-
from flask import jsonify, request, url_for, current_app


def forbbiden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def not_acceptable(message):
    response = jsonify({'error': 'not acceptable', 'message': message})
    response.status_code = 406
    return response


def method_not_allowed(message):
    response = jsonify({'error': 'method not allowed', 'message': message})
    response.status_code = 405
    return response


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def not_found(message):
    response = jsonify({'error': 'not found', 'message': message})
    response.status_code = 404
    return response


def unauthorized(message):
    response = jsonify({'status': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def suc_200(message):
    response = jsonify({'status': 'OK', 'message': message})
    response.status_code = 200
    return response


def suc_201(message):
    response = jsonify({'status': 'CREATED', 'message': message})
    response.status_code = 201
    return response


def suc_202(message):
    response = jsonify({'status': 'Accepted', 'message': message})
    response.status_code = 202
    return response


def suc_204(message):
    response = jsonify({'status': 'NO CONTENT', 'message': message})
    response.status_code = 204
    return response


def pagination_response(Model):
    page = request.args.get('page', 1, type=int)
    pagination = Model.query.paginate(page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    objs = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for(request.endpoint, page=page - 1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for(request.endpoint, page=page + 1, _external=True)
    return jsonify({'data': [obj.to_json() for obj in objs], 'prev': prev, 'next': next, 'pages': pagination.pages,
                    'count': pagination.total})
