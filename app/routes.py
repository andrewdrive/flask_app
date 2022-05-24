from flask import render_template
from app import app


@app.route('/ping', methods=['GET'])
def ping_pong():
    return '<h1>Pong!<h1>'


@app.route('/')
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


# @app.route('/login')
# def 




