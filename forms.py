from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class UrlForm(Form):
    long_url = StringField('Long url',validators=[DataRequired()])
    custom_alias = StringField('Custom alias (optional)')
 

class ChangeUrlForm(Form):
    new_long_url = StringField('Long url',validators=[DataRequired()])
    

def validate_urls(input):
    if input[0:9]=="https://" or input[0:8]=="http://":
        return input
    else:
        return "http://" + input        
