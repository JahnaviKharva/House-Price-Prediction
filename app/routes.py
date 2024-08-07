from flask import render_template, redirect, url_for
from app import app
from app.forms import HousePriceForm
import pickle
import pandas as pd

# Load the trained model
with open('model/house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HousePriceForm()
    if form.validate_on_submit():
        data = {'bedrooms': form.bedrooms.data,
                'bathrooms': form.bathrooms.data,
                'sqft_living': form.sqft_living.data,
                'location': form.location.data}
        df = pd.DataFrame([data])
        df = pd.get_dummies(df)
        df = df.reindex(columns=model.feature_names_in_, fill_value=0)
        prediction = model.predict(df)[0]
        return render_template('result.html', prediction=prediction)
    return render_template('index.html', form=form)
