from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
import joblib

app = Flask(__name__)

# Load model and scaler
model = tf.keras.models.load_model("heart_model.h5")
scaler = joblib.load("scaler.save")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Get form data
        features = [float(x) for x in request.form.values()]
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0][0]
        result = "High Risk of Heart Disease" if prediction >= 0.5 else "Low Risk of Heart Disease"
        return render_template("index.html", prediction_text=f"Prediction: {result}")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)