AUTHOR = "Jonathan Biemond"
SITENAME = "Jonathan Biemond"
SITEURL = ""
SITE_DESCRIPTION = (
    "The personal website of Jonathan Biemond. A developer and data person."
)

PATH = "content"
PAGE_PATHS = [""]
ARTICLE_PATHS = ["posts"]
TIMEZONE = "Europe/Zurich"

DEFAULT_LANG = "en"

# URL Settings
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
