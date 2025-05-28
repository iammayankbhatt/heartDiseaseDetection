from app import app, db, UserData  # Import app and models directly
import pandas as pd

def fetch_user_data():
    with app.app_context():  # Use the imported app directly
        users = UserData.query.all()
        data = [{
            'age': u.age,
            'sex': u.sex,
            'cp': u.cp,
            'trestbps': u.trestbps,
            'chol': u.chol,
            'fbs': u.fbs,
            'restecg': u.restecg,
            'thalach': u.thalach,
            'exang': u.exang,
            'oldpeak': u.oldpeak,
            'slope': u.slope,
            'ca': u.ca,
            'thal': u.thal,
            'target': 1 if float(u.target) >= 0.5 else 0  # Convert from float string to binary
        } for u in users]
        return pd.DataFrame(data)


# Load original dataset
original_df = pd.read_csv("heart.csv")

# Clean user-submitted data
df = fetch_user_data()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

valid_conditions = (
    (df['age'] >= 0) & (df['age'] <= 120) &
    (df['sex'].isin([0, 1])) &
    (df['cp'].isin([0, 1, 2, 3])) &
    (df['trestbps'] >= 80) & (df['trestbps'] <= 200) &
    (df['chol'] >= 100) & (df['chol'] <= 600) &
    (df['fbs'].isin([0, 1])) &
    (df['restecg'].isin([0, 1, 2])) &
    (df['thalach'] >= 60) & (df['thalach'] <= 220) &
    (df['exang'].isin([0, 1])) &
    (df['oldpeak'] >= 0) & (df['oldpeak'] <= 6.0) &
    (df['slope'].isin([0, 1, 2])) &
    (df['ca'].isin([0, 1, 2, 3, 4])) &
    (df['thal'].isin([0, 1, 2, 3])) &
    (df['target'].isin([0, 1]))
)

df = df[valid_conditions]

# Concatenate with original dataset
combined_df = pd.concat([original_df, df], ignore_index=True)

# Remove any duplicates just in case
combined_df.drop_duplicates(inplace=True)

# Convert categorical/discrete float columns to int
int_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
               'thalach', 'exang', 'slope', 'ca', 'thal', 'target']

for col in int_columns:
    combined_df[col] = combined_df[col].astype(int)


# Save updated dataset
combined_df.to_csv("heart.csv", index=False)
print("Updated dataset saved to heart.csv with new cleaned user data.")
