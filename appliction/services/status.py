#! -*- coding: utf-8 -*-
# Filename: status.py
"""Status Service to tell if the application is running or not"""
from falcon import HTTP_200

class StatusResource(object):
    """Status class to verify if the API is working correctly"""
    def on_get(self, req, resp):
        """Method handle GET requests"""
        resp.status = HTTP_200
        resp.body = '{"Status": "Running correctly"}'