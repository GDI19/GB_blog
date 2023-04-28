from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource

from blog.models.database import db
from blog.models import Article
from blog.schemas import ArticleSchema


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {'articles count': Article.query.count()}


class ArticleList(ResourceList):
    events = ArticleListEvents
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }