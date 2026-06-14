import sys
import json
import joblib
import pandas as pd

heart_model = joblib.load("../ai_models/heart_risk_model.pkl")
air_model = joblib.load("../ai_models/air_quality_model.pkl")
resp_model = joblib.load("../ai_models/respiratory_model.pkl")
resp_encoder = joblib.load("../ai_models/respiratory_encoder.pkl")
disease_model = joblib.load("../ai_models/disease_model.pkl")
disease_encoder = joblib.load("../ai_models/disease_encoder.pkl")

sensor_data = json.loads(sys.argv[1])

mq135 = sensor_data["mq135"]
temperature = sensor_data["temperature"]
humidity = sensor_data["humidity"]
heartRate = sensor_data["heartRate"]
spo2 = sensor_data["spo2"]

# Respiratory Model
resp_input = pd.DataFrame([{
    "spo2": spo2,
    "heartRate": heartRate,
    "temperature": temperature
}])

resp_pred = resp_model.predict(resp_input)
resp_status = resp_encoder.inverse_transform(resp_pred)[0]

# Disease Model
disease_input = pd.DataFrame([{
    "mq135": mq135,
    "temperature": temperature,
    "humidity": humidity,
    "heartRate": heartRate,
    "spo2": spo2
}])

disease_pred = disease_model.predict(disease_input)
disease_status = disease_encoder.inverse_transform(disease_pred)[0]

# Air Quality Logic
if mq135 < 150:
    air_quality = "GOOD"
elif mq135 < 250:
    air_quality = "MODERATE"
elif mq135 < 350:
    air_quality = "POOR"
else:
    air_quality = "HAZARDOUS"

# Heart Risk Logic
heart_input = pd.DataFrame([{
    "age": 50,
    "trestbps": 120,
    "chol": 200,
    "thalch": heartRate,
    "oldpeak": 1.0
}])

heart_pred = heart_model.predict(heart_input)

heart_risk = "HIGH" if heart_pred[0] > 0 else "LOW"

# Tip Guru
tip = "Maintain healthy breathing."

if spo2 < 90:
    tip = "Seek medical attention immediately."

elif air_quality == "POOR":
    tip = "Move to a better ventilated area."

elif disease_status == "Possible Asthma":
    tip = "Avoid dust and smoke exposure."

result = {
    "heartRisk": heart_risk,
    "airQuality": air_quality,
    "respiratoryStatus": resp_status,
    "diseaseRisk": disease_status,
    "tipGuru": tip
}

print(json.dumps(result))
