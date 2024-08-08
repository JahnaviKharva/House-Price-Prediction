# House-Price-Prediction
House Price Prediction Web Application
This is a web application that predicts house prices based on various features such as area, number of bedrooms, bathrooms, stories, and more. The model is trained using a Linear Regression algorithm and is deployed using Flask.

Table of Contents
Project Overview
Features
Installation
Usage
File Structure
Model Training
Deployment
Contributing
License
Project Overview
This project aims to provide an easy-to-use web interface for predicting house prices. Users can input various features of a house, and the application will predict the price based on a pre-trained model.

Features
User Input: Form to input features like area, number of bedrooms, bathrooms, stories, and more.
Prediction: Predicts the house price based on the input features using a Linear Regression model.
User-Friendly Interface: Simple and intuitive web interface.
Installation
Prerequisites
Python 3.x
pip (Python package installer)
Steps
Clone this repository:
git clone https://github.com/JahnaviKharva/House-Price-Prediction
cd house-price-prediction

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Run the Flask application:
flask run
Open your browser and go to http://127.0.0.1:5000/.

Usage
Enter the house features: Fill in the form with the house details such as area, number of bedrooms, bathrooms, etc.
Get the prediction: Click the submit button to get the predicted price of the house.
View the result: The predicted price will be displayed on the result page.
File Structure

house-price-prediction/
│
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── routes.py             # Application routes
│   └── templates/
│       ├── index.html        # Home page template
│       └── result.html       # Result page template
│
├── dataset/
│   └── Housing.csv           # Dataset used for training the model
│
├── model/
│   └── house_price_model.pkl # Trained model file
│
├── venv/                     # Virtual environment files
│
├── train_model.ipynb         # Jupyter notebook for model training
├── requirements.txt          # Python dependencies
├── app.py                    # Entry point for Flask application
├── README.md                 # This readme file
└── .gitignore                # Git ignore file
Model Training
Load the dataset: The dataset is stored in the dataset/Housing.csv file.
Preprocess the data: Categorical variables are encoded, and other necessary preprocessing steps are applied.
Train the model: A Linear Regression model is trained on the processed dataset.
Save the model: The trained model is saved as a pickle file (model/house_price_model.pkl) for use in the Flask application.
The model training script is available in train_model.ipynb. You can re-train the model by running this notebook.

Deployment
This application can be deployed on any platform that supports Flask. For example:

Deploy on Heroku
Install the Heroku CLI.

Log in to Heroku using the CLI.

Create a new Heroku app.

Push the repository to Heroku:


git push heroku main
Open the deployed application in your browser.

Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any ideas or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.
