from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from flask_login import login_required

from blog.models.user import User

users_app = Blueprint('users_app', __name__)

USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
}

@users_app.route('/', endpoint='list')
def users_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@users_app.route('/<int:user_id>/', endpoint='details')
@login_required
def user_detail(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/details.html', user=user)