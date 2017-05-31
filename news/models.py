from __future__ import unicode_literals

from mongoengine import *
import datetime


# Create your models here.
class News(EmbeddedDocument):
    meta = {
        'db_alias': 'oneline',
    }
    title = StringField()
    link = StringField()
    created = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)


class Item(Document):
    meta = {
        'db_alias': 'oneline',
    }
    content = StringField()
    comments = ListField()
    # news = EmbeddedDocument(News)

    created = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)


class Comment(Document):
    meta = {
        'db_alias': 'oneline',
    }
    item_id = StringField(required=True)
    comment_id = StringField()
    content = StringField()

    created = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)


class Feed(Document):
    meta = {
        'db_alias': 'oneline',
    }
    user_id = LongField(required=True)
    feeds = LongField()

    created = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)


class Follow(Document):
    meta = {
        'db_alias': 'user',
    }
    followed = LongField(required=True)
    follower = LongField(required=True)

    created = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)


class Salon(Document):
    meta = {
        "db_alias": "oneline",
    }

    host = LongField(required=True)
    co_host = ListField()
    discuss = ListField()  # 内为item id
    followers = ListField()
    charge = DecimalField(force_string=True)

    created = DateTimeField(default=datetime.datetime.now)
    lut = DateTimeField(default=datetime.datetime.now)
