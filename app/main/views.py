''''''
from datetime import datetime
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import main
from .forms import AddBookmarkForm
from ..models import Bookmark

@main.route('/')
def index():
    '''Main page'''
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    '''Home page'''
    form = AddBookmarkForm()
    if form.validate_on_submit():
        bookmark = Bookmark(url=form.url.data,
                            title=form.title.data,
                            description=form.description.data,
                            date_last_viewed=datetime.now())
        current_user.bookmarks.append(bookmark)
        current_user.save()
        return redirect(url_for('main.home'))
    return render_template('home.html', form=form)

@main.route('/profile')
@login_required
def profile():
    '''Profile page'''
    return render_template('profile.html')
