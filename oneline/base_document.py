# -*- coding: utf-8 -*-

from mongoengine import *
import datetime


class BaseDocument(Document):
    created = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)
