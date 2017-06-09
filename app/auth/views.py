''''''
from flask import request, redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import SigninForm, SignupForm
from ..models import User


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    '''Sign in page'''
    form = SigninForm()
    if form.validate_on_submit():
        user = User.objects.get(email=form.email.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for("main.home"))
        flash('Invalid username or password.')
    return render_template("signin.html", form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    '''Sign up page'''
    form = SignupForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.password = form.password.data
        try:
            user.save()
            # TODO: here should be some email confirmation thing
            login_user(user)
            return redirect(url_for("main.home"))
        except:
            flash('smth not ok')

    return render_template("signup.html", form=form)


@auth.route('/signout', methods=['GET', 'POST'])
@login_required
def signout():
    '''Sign out page'''
    logout_user()
    return redirect(url_for("main.index"))
