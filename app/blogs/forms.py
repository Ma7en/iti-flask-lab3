from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


# start class
class BlogsForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 50)])
    description = StringField("Name", validators=[DataRequired(), Length(2, 5000)])
    image = StringField("Image")
    submit = SubmitField("Add New")
