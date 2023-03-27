from flask import Blueprint, render_template
from .users import USERS
from werkzeug.exceptions import NotFound


articles_app = Blueprint('articles_app', __name__)


articles = [
    {'id': 0,
    'title': 'First article',
    'content': 'Compile Bootstrap with your own asset pipeline by downloading our source Sass, JavaScript, and documentation files. This option requires some additional tooling: Sass compiler for compiling Sass source files into CSS files Autoprefixer for CSS vendor prefixing Should you require our full set of build tools, they are included for developing Bootstrap and its docs, but they are likely unsuitable for your own purposes.',
    'author': 1},
    {'id': 1,
    'title': 'Second article',
    'content': 'Compile Bootstrap with your own asset pipeline by downloading our source Sass, JavaScript, and documentation files. This option requires some additional tooling: Sass compiler for compiling Sass source files into CSS files Autoprefixer for CSS vendor prefixing Should you require our full set of build tools, they are included for developing Bootstrap and its docs, but they are likely unsuitable for your own purposes.',
    'author': 1 },
    { 'id': 2,
    'title': 'Third article',
    'content': 'Compile Bootstrap with your own asset pipeline by downloading our source Sass, JavaScript, and documentation files. This option requires some additional tooling: Sass compiler for compiling Sass source files into CSS files Autoprefixer for CSS vendor prefixing Should you require our full set of build tools, they are included for developing Bootstrap and its docs, but they are likely unsuitable for your own purposes.',
    'author': 3}
    ]

@articles_app.route('/', endpoint='list')
def articles_list():
    return render_template('articles/list.html', articles=articles)


@articles_app.route('/<int:article_id>/', endpoint='details')
def article_details(article_id):
    try:
        choosen_article = articles[article_id]
        author_name = USERS[choosen_article['author']]
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    return render_template('articles/details.html', article=choosen_article, author=author_name)