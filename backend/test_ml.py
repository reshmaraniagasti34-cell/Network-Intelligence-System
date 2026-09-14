import joblib
import pandas as pd

from telemetry import generate_telemetry, set_failure


FEATURES = [
    "latency",
    "packet_loss",
    "cpu",
    "memory",
    "bandwidth",
    "interface_errors",
    "traffic"
]


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load("network_anomaly_model.pkl")

print("\n================================")
print(" TRAINED ML ANOMALY TEST")
print("================================")


# ==========================================
# GENERATE NEW FAILURE TELEMETRY
# ==========================================

set_failure(True)

telemetry = generate_telemetry()


print("\nNEW NETWORK TELEMETRY")
print("--------------------------------")

for device in telemetry:

    print(
        device["device"],
        "| Latency:", device["latency"],
        "| Packet Loss:", device["packet_loss"],
        "| CPU:", device["cpu"],
        "| Memory:", device["memory"],
        "| Bandwidth:", device["bandwidth"],
        "| Interface Errors:", device["interface_errors"],
        "| Traffic:", device["traffic"]
    )


# ==========================================
# CONVERT TELEMETRY TO DATAFRAME
# ==========================================

df = pd.DataFrame(telemetry)

X = df[FEATURES]


# ==========================================
# ML PREDICTION
# ==========================================

predictions = model.predict(X)

scores = model.decision_function(X)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n")
print("ISOLATION FOREST RESULTS")
print("--------------------------------")


for index, device in df.iterrows():

    if predictions[index] == -1:

        status = "ANOMALY"

    else:

        status = "NORMAL"


    print(
        device["device"],
        "|",
        status,
        "| ML Score:",
        round(float(scores[index]), 4)
    )


print("\n================================")
print(" ML TEST COMPLETED")
print("================================")
