from .. import *

class InstallForm(FlaskForm):
    app_name = StringField(lazy_gettext('App name'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    user = StringField(lazy_gettext('Administrative user name'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    password = PasswordField(lazy_gettext('Administrative user password'), validators=[InputRequired(message=lazy_gettext("Field required")), EqualTo('password_confirm', message=lazy_gettext("Password doesn't match!"))])
    password_confirm = PasswordField(lazy_gettext('Administrative user password confirmation'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Save'))