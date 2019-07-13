# -*- coding: utf-8 -*-
# Filename: user.py
"""User service module"""
import falcon
import json
from domain.interfaces.collection_resource import IResourceCollection
from domain.interfaces.item_resource import IResourceItem

class UserResource(IResourceItem):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        pass

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