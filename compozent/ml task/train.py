import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Load the dataset (Ensure this is the correct path to your CSV file)
data = pd.read_csv('sleeptime_prediction_dataset.csv')

# Handle missing values by filling with the median for numerical features
data.fillna(data.median(), inplace=True)

# Separate features (X) and target (y)
X = data.drop('SleepTime', axis=1)
y = data['SleepTime']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Save the trained model to a file using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
