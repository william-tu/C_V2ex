# -*- coding:utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Command
from gevent.pywsgi import WSGIServer

from app import create_app, db
from app.models import Role, User, Follow, Comments, Article, Post, UserFavorArticle, UserFavorPost

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)


class DropAndCreate(Command):
    def run(self):
        db.drop_all()
        db.create_all()


class RunServer(Command):
    def run(self):
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()


def _make_context():
    return dict(app=app, Role=Role, User=User, Follow=Follow, db=db, Comments=Comments, Article=Article, Post=Post,
                UserFavorArticle=UserFavorArticle, UserFavorPost=UserFavorPost, test_user=User.query.first(),
                test_article=Article.query.first(), test_post=Post.query.first())


manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("db", MigrateCommand)
manager.add_command("reset_database", DropAndCreate)
manager.add_command("runserver", RunServer)

if __name__ == '__main__':
    manager.run(default_command="runserver")
