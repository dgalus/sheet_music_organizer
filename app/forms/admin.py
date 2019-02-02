from app import *

class InstrumentAddForm(FlaskForm):
    name = StringField(lazy_gettext('Instrument Name'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Add'))