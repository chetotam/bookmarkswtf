''''''
from flask import render_template
from flask_login import login_required
from . import main

@main.route('/')
def index():
    '''Main page'''
    return render_template('index.html')

@main.route('/home')
@login_required
def home():
    '''Home page'''
    return render_template('home.html')
