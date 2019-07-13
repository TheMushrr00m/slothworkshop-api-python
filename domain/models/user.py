# -*- coding: utf-8 -*-
# Filename: user.py
import datetime as dt

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)
