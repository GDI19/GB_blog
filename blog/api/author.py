from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource
from blog.models.article import Article

from blog.models.database import db
from blog.models import Author
from blog.schemas import AuthorSchema


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {'author articles count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvents
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }