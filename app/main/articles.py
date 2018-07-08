# -*- coding: utf-8 -*-
from app.responses import pagination_response
from app.models import Article
from . import main


@main.route("/articles", methods=['GET'])
def get_articles():
    return pagination_response(Article)
