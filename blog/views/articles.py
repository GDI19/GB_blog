from flask import Blueprint, render_template


articles_app = Blueprint('articles_app', __name__)


articles = {

}

@articles_app.route('/', endpoint='list')
def list():
    return render_template('articles/list.html', articles=articles)