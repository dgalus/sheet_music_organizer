from .. import *

class LoginForm(FlaskForm):
    user = StringField(lazy_gettext('Username'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    password = PasswordField(lazy_gettext('Password'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Login'))