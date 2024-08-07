from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class HousePriceForm(FlaskForm):
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired()])
    bathrooms = FloatField('Bathrooms', validators=[DataRequired()])
    sqft_living = IntegerField('Living Area (sqft)', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Predict Price')
