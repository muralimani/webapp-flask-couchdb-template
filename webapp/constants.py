"Constant values."

import re

VERSION = '0.9.5'
SOURCE_URL = 'https://github.com/pekrau/webapp-flask-couchdb-template'

BOOTSTRAP_VERSION  = '4.3.1'
JQUERY_VERSION     = '3.3.1'
DATATABLES_VERSION = '1.10.18'

LOGGER_NAME = 'webapp'

NAME_RX  = re.compile(r'^[a-z][a-z0-9_-]*$', re.I)
IUID_RX  = re.compile(r'^[a-f0-9]{32,32}$', re.I)
EMAIL_RX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# CouchDB document types
DOCTYPE_USER = 'user'
DOCTYPE_LOG  = 'log'

# User roles
ADMIN = 'admin'
USER  = 'user'
USER_ROLES = (ADMIN, USER)

# User statuses
PENDING  = 'pending'
ENABLED  = 'enabled'
DISABLED = 'disabled'
USER_STATUSES = [PENDING, ENABLED, DISABLED]

# Content types
HTML_MIMETYPE = 'text/html'
JSON_MIMETYPE = 'application/json'