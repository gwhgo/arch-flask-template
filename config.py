#!/usr/bin/env python
# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "guoweihao"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or  \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    #set to False to disable a feature, which is to signal the application every 
    #time a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
