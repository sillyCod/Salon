# -*- coding: utf-8 -*-
import functools
from django.http import HttpRequest, HttpResponse


def login_check(func):
    def wrapper(*subs, **kwargs):
        if isinstance(subs[0], HttpRequest):
            login = subs[0].session.get('login')
            if not login:
                return HttpResponse('You need Login.')
            result = func(*subs, **kwargs)
            print 'After login_check call.'
            return result

    return wrapper
