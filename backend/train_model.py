import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest


# Features used by the ML model
FEATURES = [
    "latency",
    "packet_loss",
    "cpu",
    "memory",
    "bandwidth",
    "interface_errors",
    "traffic"
]


# -----------------------------------------
# Load historical normal telemetry
# -----------------------------------------

data = pd.read_csv("../data/historical_telemetry.csv")

print("Historical dataset loaded.")
print("Records:", len(data))


# -----------------------------------------
# Select ML features
# -----------------------------------------

X = data[FEATURES]


# -----------------------------------------
# Create Isolation Forest
# -----------------------------------------

model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42
)


# -----------------------------------------
# Train model
# -----------------------------------------

model.fit(X)


# -----------------------------------------
# Save trained model
# -----------------------------------------

joblib.dump(
    model,
    "network_anomaly_model.pkl"
)


print("\nModel training completed successfully.")

print(
    "Model saved as: network_anomaly_model.pkl"
)
