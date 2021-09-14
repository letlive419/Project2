from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, RadioField, SelectField, SubmitField

class studentForm(FlaskForm):
    csrf_token = 'COP4813'
    title = StringField('Enter Book title')
    author = StringField('Enter author name')
    list_title = SelectField("Genres", choices=[
        ("HardCover Fiction","HardCover Fiction"),
        ("E-book Fiction","E-book Fiction"),
        ("Paperback Nonfiction","Paperback Nonfiction"),
        ("Hardcover Advice","Hardcover Advice")
    ])
    date = DateField('DatePicker', format='%YYYY-mm-dd')

    submit = SubmitField("Submit")

