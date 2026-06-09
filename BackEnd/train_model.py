import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("gesture_data.csv", header=None)

# Split features and labels
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "gesture_model.pkl")

print("Model trained and saved!")