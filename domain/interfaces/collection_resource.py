# -*- coding: utf-8 -*-
# Filename: collection_resource.py
"""Interface HTTP Collection resource class"""
from abc import ABCMeta, abstractmethod

class IResourceCollection(metaclass=ABCMeta):
    """Collection of Resources abstract class, inherits from BaseClass
           PUT and DELETE expects query parameters in the request to function.
           POST Ignores query parameters.
           GET can work with and without query parameters.
           query params support advanced comparison like gt, gte,lt and lte
           Examples: '/residences/?opens_at__lt=08:30:00',
                    '/residences/?name__startswith=kf'
        """

    @abstractmethod
    def on_get(self, req, resp):
        """Returns a list of object based on the query,
           or returns all the records in the table
        """
        pass

    @abstractmethod
    def on_post(self, req, resp):
        """This is bulk create by default,
           it returns a list of created objects
        """
        pass