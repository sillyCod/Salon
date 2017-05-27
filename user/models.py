# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from config.config import avatar_path


class User(AbstractUser):
    phone = models.CharField(max_length=32)
    desc = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to=avatar_path)

