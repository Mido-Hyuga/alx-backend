#!/usr/bin/env python3
""" Flask app i18n"""

from flask import Flask, render_template
from flask_babel import Babel
from configs import Config

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ main class to configure languages """
    LANGUAGES = ["en", "fr"]
    babel.default_local = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@app.route("/")
def index():
    """ index route """
    return render_template('1-index.html')
