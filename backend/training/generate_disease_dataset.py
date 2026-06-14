import pandas as pd
import random

data = []

for _ in range(10000):

    mq135 = random.randint(50, 400)
    temperature = round(random.uniform(28, 40), 1)
    humidity = round(random.uniform(30, 90), 1)
    heartRate = random.randint(50, 150)
    spo2 = random.randint(70, 100)

    if spo2 < 85:
        disease = "Emergency"

    elif spo2 < 90 and heartRate > 120:
        disease = "Respiratory Distress"

    elif mq135 > 300 and spo2 < 94:
        disease = "Possible COPD"

    elif mq135 > 250 and humidity > 70:
        disease = "Possible Asthma"

    else:
        disease = "Healthy"

    data.append([
        mq135,
        temperature,
        humidity,
        heartRate,
        spo2,
        disease
    ])

df = pd.DataFrame(data, columns=[
    "mq135",
    "temperature",
    "humidity",
    "heartRate",
    "spo2",
    "disease"
])

df.to_csv("../datasets/disease_dataset.csv", index=False)

print("Disease dataset generated!")
