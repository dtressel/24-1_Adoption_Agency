from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form to add a pet."""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[
        InputRequired(),
        AnyOf(values=["dog", "cat", "porcupine"], message="We are currently only accepting dogs, cats, and porcupines.")
        ])
    photo_url = StringField("Photo URL", validators=[
        Optional(),
        URL(require_tld=True, message="Must be a valid URL.")
        ])
    age = IntegerField("Age", validators=[
        NumberRange(min=0, max=30, message="Must be a number between 0 and 30.")
        ])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """Form to edit details of pet."""

    photo_url = StringField("Photo URL", validators=[
        Optional(),
        URL(require_tld=True, message="Must be a valid URL.")
    ])
    notes = TextAreaField("Notes")
    available = RadioField("Avaialable", choices=["Yes", "No"], validators=[Optional()])
