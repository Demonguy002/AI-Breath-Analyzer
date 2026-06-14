import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_excel("../datasets/AirQualityUCI.xlsx")

# Remove missing values represented as -200
df.replace(-200, pd.NA, inplace=True)

# Keep useful columns
features = [
    "CO(GT)",
    "NOx(GT)",
    "NO2(GT)",
    "T",
    "RH"
]

df = df[features]

# Drop rows with missing values
df = df.dropna()

# Create air quality labels
def classify_air(row):
    co = row["CO(GT)"]

    if co < 2:
        return 0      # Good
    elif co < 5:
        return 1      # Moderate
    elif co < 10:
        return 2      # Poor
    else:
        return 3      # Hazardous

df["air_quality"] = df.apply(classify_air, axis=1)

X = df[features]
y = df["air_quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("\nAir Quality Model Accuracy:")
print(f"{accuracy * 100:.2f}%")

joblib.dump(model, "../models/air_quality_model.pkl")

print("\nAir Quality Model Saved!")
