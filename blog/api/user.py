from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.models.database import db
from blog.models import User
from blog.schemas import UserSchema
from blog.permissions.user import UserPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_patch': [UserPermission],
    }