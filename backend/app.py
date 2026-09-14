from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from telemetry import generate_telemetry, set_failure
from anomaly import calculate_anomaly_score
from root_cause import analyze_root_cause
from security import assess_security
from incident import generate_incident_report

import joblib
import pandas as pd


app = FastAPI(
    title="Network Intelligence System",
    description="AI-assisted network monitoring and root-cause analysis",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load("network_anomaly_model.pkl")


FEATURES = [
    "latency",
    "packet_loss",
    "cpu",
    "memory",
    "bandwidth",
    "interface_errors",
    "traffic"
]


@app.get("/")
def home():

    return {
        "system": "Network Intelligence System",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/analyze")
def analyze(failure: bool = True):

    # Generate telemetry
    set_failure(failure)

    telemetry = generate_telemetry()


    # Rule-based anomaly detection
    anomaly_results = []

    for device in telemetry:

        result = calculate_anomaly_score(device)

        anomaly_results.append(result)


    # ML detection
    df = pd.DataFrame(telemetry)

    predictions = model.predict(df[FEATURES])
    scores = model.decision_function(df[FEATURES])


    ml_results = []

    for index, device in df.iterrows():

        ml_results.append({
            "device": device["device"],
            "ml_status":
                "ANOMALY"
                if predictions[index] == -1
                else "NORMAL",
            "ml_score": round(
                float(scores[index]), 4
            )
        })


    # Root cause
    root_cause_result = analyze_root_cause(
        anomaly_results
    )


    # Security
    security_results = []

    for device in telemetry:

        security_results.append(
            assess_security(device)
        )


    # Incident report
    report = generate_incident_report(
        telemetry,
        anomaly_results,
        root_cause_result,
        security_results
    )


    return {

        "telemetry": telemetry,

        "anomaly_detection": anomaly_results,

        "ml_detection": ml_results,

        "root_cause": root_cause_result,

        "security": security_results,

        "incident": report
    }
    
    #analyse
@app.get("/dashboard")
def dashboard():

    return FileResponse(
        "frontend/index.html"
    )
