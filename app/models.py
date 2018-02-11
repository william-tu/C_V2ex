# -*- coding:utf-8 -*-
from flask import current_app
from itsdangerous import BadData, TimedJSONWebSignatureSerializer as Serializer

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True, index=True)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def from_json(self, update_msg):
        self.username = update_msg.get('username') if update_msg.get('username') else self.username
        self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def generate_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadData:
            return False
        return User.query.filter_by(id=data['id']).first()
