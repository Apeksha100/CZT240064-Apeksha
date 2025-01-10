from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

# Home route to serve the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Define the feature names in the same order as during training
    feature_names = ['WorkoutTime', 'ReadingTime', 'PhoneTime', 'WorkHours', 'CaffeineIntake', 'RelaxationTime']
    
    # Convert the input JSON into a DataFrame with the correct feature names
    features = pd.DataFrame([data], columns=feature_names)
    
    # Make the prediction
    prediction = model.predict(features)
    
    # Round the predicted value to 1 decimal place
    rounded_prediction = round(prediction[0], 1)
    
    # Return the prediction as a JSON response
    return jsonify({'Predicted Sleep Time': rounded_prediction})

if __name__ == '__main__':
    app.run(debug=True)
