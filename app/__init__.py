from flask import Flask, Response, redirect, url_for, request, session, abort, render_template, send_file, escape, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from flask_babel import Babel, gettext, lazy_gettext
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, URL, NumberRange, ValidationError, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from sqlalchemy import and_, or_
import logging, logging.config
import json
import datetime
import os
import re
import uuid
import yaml

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif', 'gif', 'pdf', 'doc', 'docx'])

UPLOAD_PATH = "app/static/files/"

app = Flask(__name__)
babel = Babel(app)
bc = Bcrypt(app)
app.config.from_object('config')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

logging.config.dictConfig(yaml.load(open('app/config/logging.conf')))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = None
login_manager.session_protection = "strong"

db = SQLAlchemy(app)
from app.models import *
from .utils import *
db.create_all()
users = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def render_t(*args, **kwargs):
    title = json.load(open("app/config/app.json"))["app_name"]
    return render_template(*args, **kwargs, title=title)

from app.forms import *
from app.controllers import *