from app import *

class InstrumentAddForm(FlaskForm):
    name = StringField(lazy_gettext('Instrument Name'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Add'))

class InstrumentEditForm(FlaskForm):
    name = StringField(lazy_gettext('Instrument Name'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Edit'))

class InstrumentHideForm(FlaskForm):
    submit = SubmitField(lazy_gettext('Hide'))

class InstrumentMakeVisibleForm(FlaskForm):
    submit = SubmitField(lazy_gettext('Make Visible'))

class CategoryAddForm(FlaskForm):
    name = StringField(lazy_gettext('Category Name'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Add'))

class CategoryEditForm(FlaskForm):
    name = StringField(lazy_gettext('Category Name'), validators=[InputRequired(message=lazy_gettext("Field required"))])
    submit = SubmitField(lazy_gettext('Edit'))

class CategoryHideForm(FlaskForm):
    submit = SubmitField(lazy_gettext('Hide'))

class CategoryMakeVisibleForm(FlaskForm):
    submit = SubmitField(lazy_gettext('Make Visible'))