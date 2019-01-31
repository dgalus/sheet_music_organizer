from flask_login import UserMixin

class UserLogin(UserMixin):
    def __init__(self, id, username, display_name):
        self.id = id
        self.username = username
        self.display_name = display_name

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