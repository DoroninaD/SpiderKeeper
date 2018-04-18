# Statement for enabling the development environment
import os

DEBUG = True

# Define the application directory


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# log
LOG_LEVEL = 'INFO'

# spider services
SERVER_TYPE = 'scrapyd'
SERVERS = ['http://localhost:6800']

# basic auth
NO_AUTH = False
BASIC_AUTH_USERNAME = 'admin'
BASIC_AUTH_PASSWORD = 'admin'
BASIC_AUTH_FORCE = True

FILES_STORAGE = 'https://s3.amazonaws.com/dds-testing-bucket/scrapy'
FILES_FORMAT = 'csv'

# DB settings

# DATABASE = {
#     'DB': 'postgresql',
#     'NAME': 'usummit_grabbers',
#     'USER': 'django_user',
#     'PASSWORD': 'django_password',
#     'HOST': '127.0.0.1',
#     'PORT': '5432',
#     'CONN_MAX_AGE': 30,
# }

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath('.'), 'SpiderKeeper.db')
# SQLALCHEMY_DATABASE_URI = '{DB}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'\
#     .format_map(DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

