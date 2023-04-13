from flask import Flask, render_template
from flask import request
from .views.users import users_app
from .views.articles import articles_app
from .views.auth import auth_app, login_manager
from .views.authors import authors_app
from .models.database import db
from flask_migrate import Migrate
from blog.security import flask_bcrypt
from blog.configs import ADMIN_PASSWORD, CONFIG_NAME


app = Flask(__name__)


migrate = Migrate(app, db, compare_type=True) # compare_type=True чтобы замечал разницу при изменении свойств колонок


cfg_name = CONFIG_NAME or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")


db.init_app(app)
login_manager.init_app(app)
flask_bcrypt.init_app(app)


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix='/articles')
app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(authors_app, url_prefix='/authors')


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    flask create-admin
    > done! created admin: <User #1 'admin'>
    """
    from blog.models import User
    admin = User(first_name='admin', email='admin@admin.com', is_staff=True)
    admin.hash_password = ADMIN_PASSWORD

    db.session.add(admin)
    db.session.commit()

    print("Created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models.tag import Tag
    
    tags = ["flask", "django", "python", "sqlalchemy", "news",]
    for tag_name in tags: 
        tag = Tag(name=tag_name)
        db.session.add(tag)
    db.session.commit()
    print ('tags created')