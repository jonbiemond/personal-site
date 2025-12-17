AUTHOR = "Jonathan Biemond"
SITENAME = "Jonathan Biemond"
SITEURL = ""
SITE_DESCRIPTION = (
    "The personal website of Jonathan Biemond. A developer and data person."
)

PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["posts"]
TIMEZONE = "Europe/Zurich"

DEFAULT_LANG = "en"

# URL Settings
PAGE_URL = "{slug}.html"
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
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

STATIC_PATHS = [
    "extra/robots.txt",
    "pdfs/biemond_jonathan_resume.pdf",
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "pdfs/biemond_jonathan_resume.pdf": {"path": "biemond_jonathan_resume.pdf"},
}
