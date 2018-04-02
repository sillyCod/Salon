# -*- coding: utf-8 -*-

from configparser import ConfigParser
import os


cfg = ConfigParser()
cfg.readfp(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.cfg')))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.cfg'))

avatar_path = cfg.get('avatar', 'img_path')
