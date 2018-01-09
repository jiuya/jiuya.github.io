#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'jiuya'
SITENAME = 'Hello Blog'
SITEURL = 'https://jiuya.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'Japanese'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/jiuya'),
          ('twitter', 'https://twitter.com/jiuya'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-themes/pelican-blue'
SIDEBAR_DIGEST = 'Embedded Programmer'
FAVICON = 'https://avatars3.githubusercontent.com/u/6884687?s=460&v=4'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
LINKS = False
TWITTER_USERNAME = 'jiuya'
MENUITEMS = (('Blog', SITEURL),)
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
