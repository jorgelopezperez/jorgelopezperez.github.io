#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jorge López Pérez'
SITENAME = 'pyadventures'
SITESUBTITLE = 'Just another blog about python, Django, data, maps and visualization'
SITEURL = ''
OUTPUT_PATH = '../output_src'
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
#ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%M}/{date:%d}/{slug}/index.html'

MENUITEMS = (
  ('Home','/'),
  #('Blog-I','/articles/'),
  #('Blog-II','/category/articles/'),
  ('About','/about/'),
  ('CV','/cv/my_cv.html')
)

LOAD_CONTENT_CACHE = False

#PLUGIN_PATHS = ["plugins", "C:\Users\usuari\pelican-addons\pelican-plugins"]
#PLUGINS = ["assets"]
PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_toc','jinja2content']
#PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#           'liquid_tags.youtube', 'liquid_tags.vimeo',
#           'liquid_tags.include_code', 'liquid_tags.notebook']

DISPLAY_CATEGORIES_ON_MENU = True

#THEME = 'pelican-bootstrap3'
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
PYGMENTS_STYLE  = 'paraiso-dark'
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'extensions': ['mdx_include'],
    'output_format': 'html5',
}

#THEME = 'Flex'
#THEME_STATIC_DIR = 'themes'
#THEME = 'themes/notmyidea'
THEME = 'themes/elegant'
STATIC_PATHS = [
    'images',
    'extra',  # this
    'css',
]

THEME_TEMPLATES_OVERRIDES = []
CSS_FILE = 'main.css'
#CSS_FILE = 'wide.css'
#CUSTOM_CSS = 'css/custom.css'

EXTRA_PATH_METADATA = {
    #'css/custom.css': {'path': 'css/custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}


TIMEZONE = 'UTC'

DEFAULT_LANG = 'es'
I18N_TEMPLATES_LANG = 'en'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/joloml'),
          ('GitHub', 'https://github.com/jorgelopezperez'),
          ('Linkedin', 'https://www.linkedin.com/in/jorgelopezph/'))
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


GOOGLE_ANALYTICS = 'UA-167966224-1'
TWITTER_USERNAME = "@jolom"
