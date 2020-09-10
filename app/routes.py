#!/usr/bin/env python
# coding=utf-8
from app import app
from flask import render_template

@app.route("/")
@app.route('/index')
def index():
    user = {'usenrmae':'Miguel'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The avengers movie is so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

