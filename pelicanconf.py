#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nix Composer'
SITENAME = 'Tech Rumblings - Unixtech'
SITEURL = 'https://unixtech.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'downloads', 'code']
CODE_DIR = 'static/code'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TWITTER_USER = "abhaytrivedi"
THEME = "pelican-octopress-theme"
SEARCH_BOX = False
#X_MIN_READ = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
LOAD_CONTENT_CACHE = False
#"Menu setting
MENUITEMS = [('About ME', '/'), ('Archives', '/archives.html')]


#Plugin things
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.include_code', 'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.notebook', 'liquid_tags.youtube', 'clean_summary', 'post_stats']
