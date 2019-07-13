# -*- coding: utf-8 -*-
# Filename: __init__.py

from falcon import API
from appliction.services.serviceregister import ServiceRegister

APP_MIDDLEWARES = []

class Application(object):
    """Application starter class"""
    def __init__(self):
        self.api = API(middleware=APP_MIDDLEWARES)
        self.api.req_options.auto_parse_form_urlencoded = True
        self.start()

    def start(self):
        """Do some configurations when the app start"""
        ServiceRegister.register_service(self.api)
