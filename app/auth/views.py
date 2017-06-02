''''''
from flask import render_template, redirect, url_for
from . import auth
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''Log in page'''
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)
