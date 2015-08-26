#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Voyager'
SITENAME = "Tech Universe"
SITEURL = 'https://unixtech.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'downloads', 'static/code']
CODE_DIR = 'static/code'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%b-%Y}/{slug}.html'
ARTICLE_URL = '{date:%b-%Y}/{slug}.html'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all-atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s-atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


FAVICON_FILENAME = 'favicon.png'
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
THEME = "themes/pelican-octopress-theme"
SEARCH_BOX = False
X_MIN_READ = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
LOAD_CONTENT_CACHE = False
#"Menu setting
MENUITEMS = [('About ME', '/pages/About Unixer.html'), ('Archives', '/archives.html')]


#Plugin things
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.include_code', 'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.notebook', 'liquid_tags.youtube', 'clean_summary', 'post_stats']

#Pure pelican specific settings
# COVER_IMG_URL = "images/3.jpg"
# PROFILE_IMAGE_URL = "images/profile.png"
