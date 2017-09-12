# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 11:14
# @File    : views.py
from django.http import HttpResponse
from .ops.auth import verify


def login(req):
    email = req.POST.get("email")
    passwd = req.POST.get("passwd")

    if not email and passwd:
        return HttpResponse("参数错误")

    if not verify(email, passwd):
        return HttpResponse("请检查邮箱和密码是否匹配")

    req.session['login'] = True

