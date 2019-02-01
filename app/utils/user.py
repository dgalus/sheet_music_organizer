from flask_login import UserMixin
from functools import wraps
from app import *

class UserLogin(UserMixin):
    def __init__(self, id, username, display_name, is_admin):
        self.id = id
        self.username = username
        self.display_name = display_name
        self.is_admin = is_admin

    def __repr__(self):
        return "UserLogin<%s, %s>" % (self.id, self.username)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


def require_is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        curr_user = User.query.filter(User.id==current_user.id).first()
        if curr_user:
            if curr_user.is_admin == True:
                return func(*args, **kwargs)
        abort(403)
    return wrapper