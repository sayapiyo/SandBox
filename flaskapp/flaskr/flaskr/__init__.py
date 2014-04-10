# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# create our little application :)
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.from_object('flaskr.config')
db = SQLAlchemy(app)
import flaskr.views

if __name__ == '__main__':
    init_db()
    app.run()
