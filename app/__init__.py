#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
#Flask-Login provides a very useful feature that forces users toi log in before they can view 
#certain pages of the appliation. If  a user who is not loged in  tries to view a protected page,
# Flask-Login will automatically redirect the user to the login form, an only redirect back to
# the page the user wanted to view after the login process is complete.
# The 'login' value is the function (or endpoint) name for the login view. In other words, the name 
# you would use in a `url_for()` call to get the URL.
login.login_view = 'login'
from app import routes, models

