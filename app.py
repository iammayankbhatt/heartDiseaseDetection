from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import tensorflow as tf
import joblib

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Load trained model and scaler
model = tf.keras.models.load_model("heart_model.h5")
scaler = joblib.load("scaler.save")

# Define database model
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Float)
    sex = db.Column(db.Float)
    cp = db.Column(db.Float)
    trestbps = db.Column(db.Float)
    chol = db.Column(db.Float)
    fbs = db.Column(db.Float)
    restecg = db.Column(db.Float)
    thalach = db.Column(db.Float)
    exang = db.Column(db.Float)
    oldpeak = db.Column(db.Float)
    slope = db.Column(db.Float)
    ca = db.Column(db.Float)
    thal = db.Column(db.Float)
    target = db.Column(db.Integer)  # Now matches the original dataset (0 or 1)

# Create database tables
with app.app_context():
    db.create_all()

# Route to home page
@app.route('/')
def home():
    return render_template("index.html")

# Route to make prediction
@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Get form inputs and convert to float
        features = [float(x) for x in request.form.values()]

        # Scale features
        features_scaled = scaler.transform([features])

        # Predict using the model
        probability = model.predict(features_scaled)[0][0]
        prediction = 1 if probability >= 0.5 else 0
        result = "High Risk of Heart Disease" if prediction == 1 else "Low Risk of Heart Disease"

        # Save input + result to database
        user_data = UserData(
            age=features[0],
            sex=features[1],
            cp=features[2],
            trestbps=features[3],
            chol=features[4],
            fbs=features[5],
            restecg=features[6],
            thalach=features[7],
            exang=features[8],
            oldpeak=features[9],
            slope=features[10],
            ca=features[11],
            thal=features[12],
            target=prediction  # Just 0 or 1
        )
        db.session.add(user_data)
        db.session.commit()

        return render_template("index.html", prediction_text=f"Prediction: {result}")

    except Exception as e:
        return f"Error: {str(e)}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
