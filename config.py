import os
import string
import random

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgres://smo:smo@127.0.0.1:5434/smo'
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))

SECRET_KEY = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))

LANGUAGES = {
    'en': 'English',
    'pl': 'Polski'
}