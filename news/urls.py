# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index$', index, name='index'),
    url(r'^create/item/$', create_item, name='create'),
    url(r"^wx_index$", wx_index, name="wx_index")
]
