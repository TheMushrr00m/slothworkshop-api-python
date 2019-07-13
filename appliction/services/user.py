# -*- coding: utf-8 -*-
# Filename: user.py
"""User service module"""
import falcon
import json
from domain.interfaces.collection_resource import IResourceCollection
from domain.interfaces.item_resource import IResourceItem
from domain.serializers.user import UserSchema
from domain.models.user import User
from marshmallow import ValidationError

class UserResource(IResourceItem):
    def __init__(self):
        pass

    def on_get(self, req, resp, user_id): # /users/:user_id
        user = User(id=user_id, name='John')
        schema = UserSchema()
        try:
            result = schema.dump(user)
            resp.body = json.dumps(result.data)
        except ValidationError as err:
            resp.body = "{\"error\": {0}}".format(err.messages)
        resp.status = falcon.HTTP_200
        return resp

    def on_put(self, req, resp):
        pass

    def on_delete(self, req, resp):
        pass

class UserCollection(IResourceCollection):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        pass

    def on_post(self, req, resp):
        pass