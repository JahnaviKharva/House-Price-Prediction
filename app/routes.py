from flask import render_template, request
from app import app
import pickle
import numpy as np

# Load the trained model
with open('C:\\Users\\Jahnavi Kharva\\house_price_prediction\\model\\house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    mainroad = 1 if request.form['mainroad'].lower() == 'yes' else 0
    guestroom = 1 if request.form['guestroom'].lower() == 'yes' else 0
    basement = 1 if request.form['basement'].lower() == 'yes' else 0
    hotwaterheating = 1 if request.form['hotwaterheating'].lower() == 'yes' else 0
    airconditioning = 1 if request.form['airconditioning'].lower() == 'yes' else 0
    parking = int(request.form['parking'])
    prefarea = 1 if request.form['prefarea'].lower() == 'yes' else 0
    furnishingstatus = request.form['furnishingstatus'].lower()

    # Apply the same preprocessing steps
    furnishingstatus_encoded = [0, 0]
    if furnishingstatus == 'semi-furnished':
        furnishingstatus_encoded[0] = 1
    elif furnishingstatus == 'furnished':
        furnishingstatus_encoded[1] = 1
    features = np.array([[
        area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
        hotwaterheating, airconditioning, parking, prefarea,
        furnishingstatus_encoded[0], furnishingstatus_encoded[1]
    ]])
    
     # Print the features to debug
    print("Features:", features)

    try:
        prediction = model.predict(features)
        price = round(prediction[0], 2)
        print("Prediction:", prediction)
        print(f"Rendering template with price: {price}")

        return render_template('result.html', price=price)

    except Exception as e:
        print("Error during prediction:", e)
        return render_template('result.html', price="Error")
        
    
    
