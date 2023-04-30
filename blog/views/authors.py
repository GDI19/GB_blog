from flask import Blueprint, render_template
from blog.models.author import Author
from werkzeug.exceptions import NotFound


authors_app = Blueprint('authors_app', __name__)

@authors_app.route('/', endpoint='list')
def authors_list():
    authors = Author.query.all()
    return render_template('authors/list.html', authors=authors)


@authors_app.route('<int:author_id>', endpoint='details')
def author_detail(author_id):
    author = Author.query.filter_by(id=author_id).one_or_none()
    if author is None:
        raise NotFound(f"Author #{author_id} doesn't exist!")
    return render_template('authors/details.html', author=author)