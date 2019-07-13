# -*- coding: utf-8 -*-
# Filename: serializer.py

from marshmallow import Schema, fields

class BaseSerialize(Schema):
    """Base Entity Serializer"""
    class Meta:
        ordered = True
        strict = True

    id = fields.Int(dump_only=True)
    createdAt = fields.DateTime(dump_only=True)
    deletedAt = fields.DateTime(dump_only=True)
    updatedAt = fields.DateTime(dump_only=True)
    active = fields.Boolean(attribute='isActive', load_only=True)