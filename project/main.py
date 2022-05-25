from flask import Blueprint
from . import db
from project.models import User
from 


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index'


if __name__ == "__main__":

    app.run(debug=True, host='localhost', port=8000)





# # This func for -c 'flask shell' usage
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User}
