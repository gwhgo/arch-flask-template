#!/usr/bin/env python
# coding=utf-8
from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

#Flask-Login
#Expects certain properties and methods to be implemented in it. 
# four required items are listed below:
# - is_authenticated : a property that is True if the user has valid credentials or False otherwise
# - is_active: a property that is True if the user's account is active or False otherwise
# - is anonymouse : a property that is False foir regular users, and True for a special anonymouse user
# - get_id(): a method that returns a unique identifier for the user as a string
#Flask-Login provides a mixin class called `UserMixin`` that includes generic implementations that are appropriate
# for most user model classes. 
# Mixin : In object-oriented programming languages, a mixin(or mix-in) is a class that contains methods
# for use by other classes without having to be the parent of those of those other classes.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # 1 - Many : Please define a relationship in 1 side, and define backref
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    #more interesting profiles
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def  avatar(self,size):
        gravatar_url = 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return gravatar_url.format(digest,size)

#Flask-Login keeps track of the logged in user by storing its unique identifier in Flask's user session,
#a storage space assigned to each user who connects to the application. Each time the logged-in user
#navigates to the new page, Flask-Login retrieves the ID of the user from the session, and then loads 
# that user into memory. 
# Because Flask-Login knows nothing about databases, it need=s the application's help in loading a user.
# For that reason, the extension expects that the appilation will configure a user loader function, 
# that can be called to load a user given the ID.
# The user loader is registered with Flask-Login iwth the @login.user_loader decorator.
# The id that Flask-Login passes to the function as an argument is goint to be a string,
# so databases that use nemeric IDs need to convert the string to integer as you see above. 
@login.user_loader
def load_user(id):
    return User.query.get(int(id))






# User - Post  <=> 1 - Many 
#  1 - Many: Please defined a column in many side.
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    
