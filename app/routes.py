from crypt import methods
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, PassDataForm


@app.route('/ping', methods=['GET'])
def ping_pong():
    return '<h1>Pong!<h1>'


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.name.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/passdata', methods=['POST'])
def pass_data():
    form = PassDataForm()
    #if form.validate_on_submit():
    pass



