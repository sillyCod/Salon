# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 13:57
# @File    : auth.py


import hashlib
from user.models import User


def verify(email, passwd):
    user = User.objects(email=email, password=passwd)
    if not user:
        return False
    return True
