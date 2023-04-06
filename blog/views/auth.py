from flask import Blueprint, current_app, render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError

from blog.forms.user import RegistrationForm, LoginForm
from blog.models import User
from blog.models.database import db


auth_app = Blueprint('auth_app', __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route('/signup/', methods=['GET', 'POST'], endpoint='signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    error = None
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username already exists!")
            return render_template('auth/register.html', form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template('auth/register.html', form=form)
    
        user = User(username=form.username.data,
                    first_name=form.first_name.data,
                    last_name = form.last_name.data,
                    email = form.email.data,
                    is_staff = False,)
        user.hash_password = form.password.data
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info("Created user %s", user)
            login_user(user)
            return redirect(url_for("index"))
        
    return render_template("auth/register.html", form=form, error=error)



@auth_app.route('/login/', methods=['GET', 'POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    error = None
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user and user.validate_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = 'invalid username or password'

        
    return render_template('auth/login.html', form=form, error=error)


@auth_app.route('/logout/', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



__all__ = [
    "login_manager",
    "auth_app",
]