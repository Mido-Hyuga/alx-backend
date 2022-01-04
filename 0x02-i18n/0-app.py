#!/usr/bin/env python3
""" Flask app i18n"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """ Index render """
    return render_template('0-index.html')
