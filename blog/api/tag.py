from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.models.database import db
from blog.schemas import TagSchema
from blog.models import Tag


class Taglist(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }