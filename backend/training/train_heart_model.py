import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../datasets/heart_disease_uci.csv")

# Convert target column
df["num"] = df["num"].apply(lambda x: 1 if x > 0 else 0)

# Remove unnecessary columns
drop_cols = ["id", "dataset"]
for col in drop_cols:
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)

# Convert categorical columns
df = pd.get_dummies(df)

# Fill missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# Features and target
X = df.drop("num", axis=1)
y = df["num"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nHeart Risk Model Accuracy:")
print(f"{accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "../models/heart_risk_model.pkl")

print("\nModel saved successfully!")
