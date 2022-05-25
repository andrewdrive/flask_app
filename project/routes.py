from crypt import methods
from flask import render_template, flash, redirect
from flask_login import login_required
from project import app, login_manager
from project.forms import LoginForm, PassDataForm
from project.models import db, User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PassDataForm()
   


    return render_template('index.html', title='Home', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """For GET requests, display the login form.
    For POSTS, login the current user by processing the form.
    """
    print(db)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.username.data)
        if user:
            pass
    
    return render_template('login.html', title='Login', form=form)



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}'.format(form.name.data))
#         return redirect('/index')
#     return render_template('login.html', title='Sign In', form=form)



# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return '<h1>Pong!<h1>'
