# -*- coding:utf-8 -*-
from datetime import datetime

from flask import current_app, url_for
from itsdangerous import BadData, TimedJSONWebSignatureSerializer as Serializer

from app import db
from app.exceptions import ValidationError


class SaveMixin(object):

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Permission(object):
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_ARTICLES_COMMENTS = 0x08
    ADMINISTER = 0x80

    @staticmethod
    def to_json():
        return {'FOLLOW': Permission.FOLLOW,
                'COMMENT': Permission.COMMENT,
                'WRITE_ARTICLES': Permission.WRITE_ARTICLES,
                'MODERATE_ARTICLES_COMMENTS': Permission.MODERATE_ARTICLES_COMMENTS,
                'ADMINISTER': Permission.ADMINISTER
                }


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)
    default = db.Column(db.Boolean)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
            'Moderate': (
                Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES |
                Permission.MODERATE_ARTICLES_COMMENTS, False),
            'Admin': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True, index=True)
    avatar = db.Column(db.String(255), default="http://pbuf1enju.bkt.clouddn.com/default_avatar.png")
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    comments = db.relationship('Comments', backref='author', lazy='dynamic')
    followed = db.relationship('Follow', foreign_keys=[Follow.follower_id],
                               backref=db.backref('follower', lazy='joined'), lazy='dynamic',
                               cascade='all, delete-orphan')
    followers = db.relationship('Follow', foreign_keys=[Follow.followed_id],
                                backref=db.backref('followed', lazy='joined'), lazy='dynamic',
                                cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            else:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'avatar': self.avatar,
            'posts': url_for('main.get_user_posts', id=self.id, _external=True)
        }

    def from_json(self, update_msg):
        self.username = update_msg.get('username') if update_msg.get('username') else self.username
        self.avatar = update_msg.get('avatar') if update_msg.get("avatar") else self.avatar
        self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
        if not self.username:
            self.username = current_app.config["USERNAME_PREFIX"] + '_' + str(self.id)
            db.session.add(self)
            db.session.commit()

    def generate_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except BadData:
            return None
        return User.query.filter_by(id=data['id']).first()

    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)
            db.session.commit()

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)
            db.session.commit()

    def is_following(self, user):
        return self.followed.filter_by(followed_id=user.id).first() is not None

    def is_followed_by(self, user):
        return self.followers.filter_by(follower_id=user.id).first() is not None


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    update = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comments', backref='posts', lazy='dynamic')
    cover_image = db.Column(db.String(128))  # 封面图片

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created': self.created,
            'update': self.update,
            'author': url_for('main.get_user', id=self.author_id, _external=True),
            'cover_image': self.cover_image
        }

    @staticmethod
    def from_json(json_post):
        body = json_post.get('body')
        title = json_post.get('title')
        if not body or not title:
            raise ValidationError('post does not have body or title')
        return Post(title=title, body=body)

    def save(self):
        if not self.cover_image:
            from lxml import etree
            selector = etree.HTML(self.body)
            s = selector.xpath('//img/@src')
            if s:
                self.cover_image = s.pop(0)
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    update = db.Column(db.DateTime, default=datetime.now)
    disable = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def to_json(self):
        return {
            'id': self.id,
            'body': self.body,
            'created': self.created,
            'update': self.update,
            'disable': self.disable,
            'author': url_for('main.get_user', id=self.author_id, _external=True),
            'post': url_for('main.get_post', id=self.post_id, _external=True)
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.String(128), unique=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text)
    message_url = db.Column(db.String(128))
    image_url = db.Column(db.String(128))
    add_time = db.Column(db.DateTime, default=datetime.now)
    source_from = db.Column(db.String(64), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'message_url': self.message_url,
            'image_url': self.image_url,
            'add_time': self.add_time.strftime('%Y-%m-%d %H:%M:%S'),
            'source_from': self.source_from,
        }
