import pandas as pd
import random

data = []

for _ in range(5000):

    spo2 = random.randint(70, 100)
    hr = random.randint(50, 140)
    temp = round(random.uniform(28, 40), 1)

    if spo2 >= 95 and hr < 100:
        status = "NORMAL"

    elif spo2 >= 90:
        status = "WARNING"

    else:
        status = "CRITICAL"

    data.append([spo2, hr, temp, status])

df = pd.DataFrame(
    data,
    columns=[
        "spo2",
        "heartRate",
        "temperature",
        "status"
    ]
)

df.to_csv(
    "../datasets/respiratory_dataset.csv",
    index=False
)

print("Respiratory dataset generated!")
