from flask import Flask, render_template
from flask import request
from .views.users import users_app
from .views.articles import articles_app
from .views.auth import auth_app, login_manager
from .models.database import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/blog.db'
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix='/articles')
app.register_blueprint(auth_app, url_prefix='/auth')


@app.cli.command("init_db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print('init db done!')


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username='admin', is_staff=True)
    james = User(username='James')

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("Users've been created", admin, james)

@app.route('/')
def index():
    return render_template('index.html')