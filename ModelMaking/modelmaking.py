import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Step 1: Load and preprocess the training data
df = pd.read_csv("TrainDataSet.csv")

# Convert DateTime column, let pandas infer the format
df['DateTime'] = pd.to_datetime(df['DateTime'])  # Let pandas infer the date format

# Extract additional features
df['Hour'] = df['DateTime'].dt.hour
df['DayOfWeek'] = df['DateTime'].dt.dayofweek
df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)
df['Month'] = df['DateTime'].dt.month

# Select features and target variable
features = ['Junction', 'Hour', 'DayOfWeek', 'IsWeekend', 'Month']
X = df[features]
y = df['Vehicles']

# Step 2: Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the model
model = XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1)
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_val)
mae = mean_absolute_error(y_val, y_pred)
print(f"Mean Absolute Error (MAE) on validation set: {mae}")

# Step 5: Save the model using joblib
joblib.dump(model, 'traffic_forecasting_model.pkl')

# Step 6: Read the Test dataset
test_df = pd.read_csv("TestDataSet.csv")

# Convert the DateTime column, let pandas infer the format
test_df['DateTime'] = pd.to_datetime(test_df['DateTime'])  # Let pandas infer the date format

# Extract additional features for the test data
test_df['Hour'] = test_df['DateTime'].dt.hour
test_df['DayOfWeek'] = test_df['DateTime'].dt.dayofweek
test_df['IsWeekend'] = test_df['DayOfWeek'].apply(lambda x: 1 if x >= 5 else 0)
test_df['Month'] = test_df['DateTime'].dt.month

# Use the same feature set for testing as in training
X_test = test_df[features]

# Make predictions using the trained model
test_df['PredictedVehicles'] = model.predict(X_test)

# Save the predictions to a new CSV file
test_df[['ID', 'PredictedVehicles']].to_csv('submission.csv', index=False)

print("Predictions saved to submission.csv")
