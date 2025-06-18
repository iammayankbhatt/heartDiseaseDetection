import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model # type: ignore
import joblib

# Load test data
df = pd.read_csv('testdata.csv')

# Separate features and labels
X = df.drop('target', axis=1)
y_true = df['target'].values

# Load scaler and scale the features
scaler = joblib.load('scaler.save')
X_scaled = scaler.transform(X)

# Load trained model
model = load_model('heart_model.h5')

# Make predictions
y_pred_prob = model.predict(X_scaled)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()

# Initialize counters
correct_low = wrong_low = 0
correct_high = wrong_high = 0

# Compare predictions
for true, pred in zip(y_true, y_pred):
    if true == 0:
        if pred == 0:
            correct_low += 1
        else:
            wrong_low += 1
    elif true == 1:
        if pred == 1:
            correct_high += 1
        else:
            wrong_high += 1

# Print results
print(f"Target = 0 (Low Risk):")
print(f"  Correct: {correct_low}")
print(f"  Wrong:   {wrong_low}")

print(f"\nTarget = 1 (High Risk):")
print(f"  Correct: {correct_high}")
print(f"  Wrong:   {wrong_high}")
