# -*- coding:utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)


def _make_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run(default_command="runserver")
