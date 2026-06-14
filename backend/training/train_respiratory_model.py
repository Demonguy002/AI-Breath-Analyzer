import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../datasets/respiratory_dataset.csv")

encoder = LabelEncoder()

df["status"] = encoder.fit_transform(df["status"])

X = df[[
    "spo2",
    "heartRate",
    "temperature"
]]

y = df["status"]

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

acc = accuracy_score(y_test, pred)

print("\nRespiratory Model Accuracy:")
print(f"{acc * 100:.2f}%")

joblib.dump(
    model,
    "../models/respiratory_model.pkl"
)

joblib.dump(
    encoder,
    "../models/respiratory_encoder.pkl"
)

print("\nRespiratory Model Saved!")
