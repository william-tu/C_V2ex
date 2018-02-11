# -*- coding:utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Command

from app import create_app, db

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)


class DropAndCreate(Command):
    def run(self):
        db.drop_all()
        db.create_all()


def _make_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("db", MigrateCommand)
manager.add_command("resetDB", DropAndCreate)

if __name__ == '__main__':
    manager.run(default_command="runserver")
