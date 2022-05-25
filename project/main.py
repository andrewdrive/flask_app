from flask import (Blueprint,
                   render_template,
                   redirect,
                   url_for,
                   request,
                   flash)
from . import db
from flask_login import login_required, current_user
from .models import Inputs

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/inputs', methods=['POST'])
@login_required
def inputs():
    name = request.form.get('name')
    surname = request.form.get('surname')
    inp = Inputs(name=name, surname=surname, user_id=current_user.id)
    db.session.add(inp)
    db.session.commit()
    flash('Credits were added in db.')
    return redirect(url_for('main.index'))

