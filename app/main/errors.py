# -*- coding:utf-8 -*-
from . import main
from app.exceptions import ValidationError
from app.responses import bad_request, not_found


@main.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])


@main.errorhandler(404)
def validation_error(e):
    return not_found(str(e))
