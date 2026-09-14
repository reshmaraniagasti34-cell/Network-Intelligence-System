# ml_anomaly.py

import pandas as pd

from sklearn.ensemble import IsolationForest


FEATURES = [
    "latency",
    "packet_loss",
    "cpu",
    "memory",
    "bandwidth",
    "interface_errors",
    "traffic"
]


def detect_ml_anomalies(telemetry):
    """
    Detect unusual network behavior using Isolation Forest.
    """

    df = pd.DataFrame(telemetry)

    # Select network features
    X = df[FEATURES]

    # Isolation Forest
    model = IsolationForest(
        n_estimators=100,
        contamination=0.25,
        random_state=42
    )

    model.fit(X)

    # Prediction:
    #  1  = normal
    # -1  = anomaly
    predictions = model.predict(X)

    # Anomaly score
    scores = model.decision_function(X)

    results = []

    for index, device in df.iterrows():

        if predictions[index] == -1:
            status = "ANOMALY"
        else:
            status = "NORMAL"

        results.append({
            "device": device["device"],
            "ml_status": status,
            "ml_score": round(float(scores[index]), 4)
        })

    return results
