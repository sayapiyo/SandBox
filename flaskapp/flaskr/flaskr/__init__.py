# -*- coding: utf-8 -*-
import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
         render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy

# create our little application :)
app = Flask(__name__)
db = SQLAlchemy(app)
import flaskr.views

# Load default config and override config from an environment variable
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskr.db',
    SECRET_KEY='development key',
    DEBUG=True,
    USERNAME='admin',
    PASSWORD='default'
    ))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

if __name__ == '__main__':
    init_db()
    app.run()
