#!/usr/bin/env python
# coding=utf-8

from .base import db


def init_app(app):
    db.init_app(app)
