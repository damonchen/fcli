#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template

home_bp = Blueprint(__name__)


@home_bp.route('/')
def index():
    return render_template('index.html')
