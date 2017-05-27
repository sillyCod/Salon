# -*- coding: utf-8 -*-

import datetime


def strftime(date, timeformat="%Y%m%d"):
    if not isinstance(date, datetime.datetime):
        print "Class Type is not a datetime.Please Verify it."
        return
    return date.strftime(timeformat)
