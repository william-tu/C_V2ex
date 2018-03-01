# -*- coding:utf-8 -*-
from collections import Iterable
from functools import wraps
from models import Permission
from flask import request, g

from responses import not_acceptable, bad_request, forbbiden


def json_field_acceptable(iterable_field, iterable_methods=[]):
    """
    检查请求的类型以及字段
    :param iterable_field:可迭代的字段集合
    :param iterable_methods: 可迭代的请求方法集合
    :return:
    """
    if not isinstance(iterable_field, Iterable):
        raise TypeError('the type of param is not iterable')

    def acceptable(f):
        @wraps(f)
        def decorate(*args, **kwargs):
            if request.method not in iterable_methods:
                return f(*args, **kwargs)
            if not request.json:
                return not_acceptable('data type is not json')
            for i in iterable_field:
                if not request.json.get(i):
                    return bad_request('params error')
            return f(*args, **kwargs)

        return decorate

    return acceptable


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbbiden('permission not match')
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
