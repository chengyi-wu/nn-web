from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html', current_time=datetime.utcnow())