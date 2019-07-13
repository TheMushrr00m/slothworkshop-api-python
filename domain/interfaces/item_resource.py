# -*- coding: utf-8 -*-
# Filename: item_resource.py
from abc import ABCMeta, abstractmethod

class IResourceItem(metaclass=ABCMeta):
    """Single resource abstract class,
       This uses the Falcon event handlers to manage GET, PUT, DELETE
       POST is not supported here since its a change that affect a Collection.
       Each method expects obj_id to the request uri.
    """

    @abstractmethod
    def on_get(self, req, resp):
        """Returns a single record using its id"""
        pass

    @abstractmethod
    def on_put(self, req, resp):
        """Returns the number of rows updated 1 is successful 0 is failed update"""
        pass

    @abstractmethod
    def on_delete(self, req, resp):
        """Returns the number of rows deleted 1 is successful 0 is failed update"""
        pass

