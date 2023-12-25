"""Forms for Flask Cafe."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, URL, Optional

class CafeForm(FlaskForm):
    """Form for adding/editing cafes"""

    name = StringField("Name", validators=InputRequired())

    description = TextAreaField(
        "Description",
        validators=[Optional(), Length(max=300)]
    )

    url = StringField(
        'URL',
        validators=[Optional(), URL(), Length(max=500)]
    )

    address = StringField(
        "Address",
        validators=[InputRequired(), Length(max=120)]
    )

    #FIXME: Do I need coerce=int? What does it do?

    city_code = SelectField("City Code", coerce=int)

    image_url = StringField(
        'Image URL',
        validators=[Optional(), URL(), Length(max=500)]
    )
