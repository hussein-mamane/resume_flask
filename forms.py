from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import DataRequired


class FeedBackForm(FlaskForm):
    full_name = StringField('Name', validators=[DataRequired(),
                                                validators.Length(min=6, max=35)])
    feedback = TextAreaField('Feedback', validators=[DataRequired(),
                                                     validators.Length(min=3, max=200)])
#  render_kw={"id": "feedback-form"}
