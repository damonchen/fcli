#!/usr/bin/env python
# coding=utf-8


from flask import Flask
import os


def create_app(config=None):
    from . import models, routes, services
    app = Flask(__name__)

    # load default configuration
    app.config.from_object('{{project}}.settings')
    # load environment configuration
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    # load app sepcified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    return app
