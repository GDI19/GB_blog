from flask import Blueprint, redirect, render_template, request, url_for, current_app
from werkzeug.exceptions import NotFound
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from blog.models.author import Author
from blog.models.article import Article
from blog.forms.articles import CreateArticleForm
from blog.models.database import db
from blog.models.tag import Tag

articles_app = Blueprint('articles_app', __name__)


"""articles = [
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
"""
@articles_app.route('/', endpoint='list')
def articles_list():
    articles = Article.query.all()
    return render_template('articles/list.html', articles=articles)


@articles_app.route('/<int:article_id>/', endpoint='details')
@login_required
def article_details(article_id):
    choosen_article=Article.query.filter_by(id=article_id).options(
        joinedload(Article.tags)
        ).one_or_none()
    if choosen_article is None:
        raise NotFound(f'The article #{article_id} does not exist!')
    return render_template('articles/details.html', article=choosen_article)


@articles_app.route('/create/', methods=['GET', 'POST'], endpoint='article_create')
@login_required
def article_create():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if request.method == "POST" and form.validate_on_submit:
        _article = Article(title = form.title.data, text = form.text.data)
        db.session.add(_article)

        if current_user.author:
            _article.author = current_user.author
        else:
            author = Author(id_user=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author = author

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create a new article!"
        else:    
            return redirect(url_for('articles_app.details', article_id=_article.id))

    return render_template('articles/create.html', form = form, error=error)