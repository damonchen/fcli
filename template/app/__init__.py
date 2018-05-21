#!/usr/bin/env python
# coding=utf-8

from flask import Flask


def create_app():
    from . import db, auth, blog
    app = Flask(__name__)
    db.init_app(app)
    auth.init_app(app)
    blog.init_app(app)
    return app
