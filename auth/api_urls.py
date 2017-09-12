# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 11:12
# @File    : api_urls.py

from django.conf.urls import url
from .views import login

urlpatterns = [
    url(r'^$', login, name="login"),
]