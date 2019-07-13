#! -*- coding: utf-8 -*-
# Filename: service_register.py
from appliction.services.status import StatusResource

class ServiceRegister(object):
    """Service register class"""
    @staticmethod
    def register_service(api):
        """Public method to register services (Inject dependencies)"""
        api.add_route('/', StatusResource())