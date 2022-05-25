from flask import Blueprint, render_template, redirect, url_for
from . import db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


@main.route('/inputs', methods=['POST'])
def inputs():
    return redirect(url_for('main.index'))


# if __name__ == "__main__":
#     app.run(debug=True, host='localhost', port=8000)
#
#

# # This func for -c 'flask shell' usage
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User}
