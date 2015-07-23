
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Evan Misshula'
SITENAME = u"Evan Misshula"
SITEURL = ''

PATH = 'content'
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Bio','/pages/bio.html'),
             ('Academic','/pages/academic.html'),
             ('Contact','/pages/contact.html'),]

TIMEZONE = 'US/Eastern'

PELICAN_THEMES = '/home/evan/pelican-themes/crowsfeat'
DELETE_OUTPUT_DIRECTORY = False
USE_FOLDER_AS_CATEGORY = True

DEFAULT_LANG = u'en'
STATIC_PATHS = [ 'images', 'js','extra']
IGNORE_FILES = ['.#*', '*~']
GITHUB_URL = 'http://github.com/EvanMisshula/'



TWITTER_USERNAME = 'EMisshula'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('juan reyero', 'http://juanreyero.com/about/'),
         ('Sasha Chua','http://sachachua.com/blog/'),
         ('org-mode tutorials', 'http://orgmode.org/worg/org-tutorials/index.html'),
         ('emacsnyc.org','http://emacsnyc.org'),
         ('Bastien Guerry','http://bzg.fr/index.en.html'),
         ('ian barton','http://ianbarton.net/'),
         ('Fernando Perez','http://blog.fperez.org/'),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/emisshula'),
          ('github', 'https://github.com/EvanMisshula'),
          ('linkedin','http://www.linkedin.com/pub/evan-misshula/20/5b/810‎'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
