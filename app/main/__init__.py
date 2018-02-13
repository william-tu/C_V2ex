# -*- coding:utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)

from . import auth, users, comments, follow, posts, errors
