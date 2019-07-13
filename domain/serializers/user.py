# -*- coding: utf-8 -*-
# Filename: user.py
"""User Entity Serializer"""

from marshmallow import fields
from domain.interfaces.serializer import BaseSerialize

class UserSchema(BaseSerialize):
    name = fields.Str()