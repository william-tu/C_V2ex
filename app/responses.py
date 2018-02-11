# -*- coding:utf-8 -*-
from flask import jsonify


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
