from crypt import methods
from flask import render_template, flash, redirect
from flask_login import login_required
from app import app, login_manager
from app.forms import LoginForm, PassDataForm
from app.models import db, User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return '<h1>Pong!<h1>'


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




@app.route('/passdata', methods=['POST'])
@login_required
def pass_data():
    form = PassDataForm()
    #if form.validate_on_submit():
    pass


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}'.format(form.name.data))
#         return redirect('/index')
#     return render_template('login.html', title='Sign In', form=form)
