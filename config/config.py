# -*- coding: utf-8 -*-

import six
if six.PY2:
    import ConfigParser as configparser
elif six.PY3:
    import configparser
import os


cfg = configparser.ConfigParser()
cfg.read_file(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.cfg')))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.cfg'))

avatar_path = cfg.get('avatar', 'img_path')
