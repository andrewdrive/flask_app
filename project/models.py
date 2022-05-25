from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % self.name


class Inputs(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Inputs %r>' % self.name


# from project import db, create_app, models
# db.create_all(app=create_app())


# # pass the create_app result so Flask-SQLAlchemy gets the configuration.
