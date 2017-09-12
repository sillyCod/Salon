# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 16:14
# @File    : views.py
from django.shortcuts import render_to_response


def login(req):
    return render_to_response("index.html")

