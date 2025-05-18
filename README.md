# 🫀 Heart Disease Detection using Machine Learning

This project uses machine learning techniques to predict the likelihood of heart disease in a patient based on health-related input data. It’s built using Python, scikit-learn, and standard data science libraries, and demonstrates how data-driven models can assist in early diagnosis and medical decision-making.

---

## 🚀 Features

- Predicts presence of heart disease using various clinical parameters
- Cleaned and preprocessed dataset
- Trained using Logistic Regression and Random Forest
- Evaluation through accuracy score, confusion matrix, and classification report
- Simple and readable code for educational purposes

---

## 📁 Project Structure

heart_disease_project/               # ← project root
│
├── app.py                           # main Flask application
├── heart.csv                        # heart disease dataset
├── requirements.txt                 # Python dependencies
│-- train_model.py
├── templates/                       # Jinja2 HTML templates
│   └── index.html
│
├── static/                          # all publicly served assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── img/
│       └── bg.jpg       # the futuristic heart background
│
└── README.md                        # project overview & run instructions




---

## 🧪 How It Works

1. Load the dataset and perform exploratory data analysis (EDA)
2. Clean and preprocess the data (null checks, normalization, etc.)
3. Split into training and test sets
4. Train models (e.g., Logistic Regression, Random Forest)
5. Evaluate performance using standard classification metrics

---

## 📊 Sample Input Features

- Age
- Sex
- Chest pain type
- Resting blood pressure
- Cholesterol level
- Fasting blood sugar
- Maximum heart rate
- ST depression (oldpeak)
- Number of major vessels
- Thalassemia

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   
   git clone https://github.com/iammayankbhatt/heartDiseaseDetection.git
   cd heartDiseaseDetection
Create and activate a virtual environment (recommended)




python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies




pip install -r requirements.txt
Run the notebook
Open heart_disease_detection.ipynb in Jupyter Notebook or VS Code and run the cells.

🧠 Model Performance
The models are evaluated using:

Accuracy Score

Confusion Matrix

Precision, Recall, F1 Score

Note: Performance may vary depending on preprocessing steps and train/test split.

📚 Dataset
The dataset used in this project is publicly available and contains clinical records related to heart disease diagnosis. It includes both categorical and numerical features.