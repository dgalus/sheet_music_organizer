from ..  import *

class SearchForm(FlaskForm):
    search_field = StringField(lazy_gettext('Search'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Search'))