import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("../datasets/disease_dataset.csv")

encoder = LabelEncoder()

df["disease"] = encoder.fit_transform(df["disease"])

X = df[
    [
        "mq135",
        "temperature",
        "humidity",
        "heartRate",
        "spo2"
    ]
]

y = df["disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("\nDisease Risk Model Accuracy:")
print(f"{acc * 100:.2f}%")

joblib.dump(
    model,
    "../models/disease_model.pkl"
)

joblib.dump(
    encoder,
    "../models/disease_encoder.pkl"
)

print("\nDisease Model Saved!")
