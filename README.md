# Network Intelligence System

## 1. Overview

The **Network Intelligence System** is a prototype designed to transform raw network telemetry into actionable and explainable network intelligence.

Traditional network monitoring can detect when a metric crosses a threshold, but it does not always explain:

- What caused the problem?
- Which device is the probable root cause?
- Which other devices are affected?
- Is the problem operational or potentially security-related?
- How confident is the system in its conclusion?

This project addresses these questions through a complete pipeline:

**Network Telemetry → Data Processing → Anomaly Detection → Root-Cause Analysis → Security Assessment → Incident Report**

---

## 2. Problem Statement

Modern computer networks continuously generate telemetry such as:

- Latency
- Packet loss
- Bandwidth utilization
- CPU utilization
- Memory utilization
- Interface errors
- Traffic statistics

A simple threshold-based monitoring system may report that packet loss has increased on a device. However, network administrators need more useful information about the cause, impact, and security significance of the incident.

The goal of this prototype is therefore to demonstrate engineering reasoning rather than simple threshold monitoring.

---

## 3. Objectives

The system aims to:

1. Generate and process network telemetry.
2. Detect abnormal network behavior.
3. Identify the probable root-cause device.
4. Identify affected network components.
5. Distinguish operational anomalies from potential security-related anomalies.
6. Provide a confidence score for root-cause analysis.
7. Generate an explainable incident report.
8. Demonstrate both rule-based and machine-learning anomaly detection.

---

## 4. System Architecture

```text
                 Network Telemetry
                        |
                        v
                Data Processing
                        |
              +---------+---------+
              |                   |
              v                   v
       Rule-Based Detection   ML Detection
                              Isolation Forest
              |                   |
              +---------+---------+
                        |
                        v
                Root-Cause Analysis
                        |
                        v
                Security Assessment
                        |
                        v
                 Incident Report
                        |
                        v
                 FastAPI Dashboard
```

---

## 5. Technology Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pandas
- NumPy
- Scikit-learn
- NetworkX
- Joblib

### Frontend

- HTML
- CSS
- JavaScript

### Machine Learning

- Isolation Forest
- Unsupervised anomaly detection

---

## 6. Project Structure

```text
Network Intelligence System/
│
├── backend/
│   ├── app.py
│   ├── frontend/
│   │   └── index.html
│   ├── historical_data.py
│   ├── train_model.py
│   ├── test_ml.py
│   ├── test_incident.py
│   ├── network_anomaly_model.pkl
│   └── venv/
│
├── README.md
└── presentation/
```

> The exact filenames may differ depending on the final project version.

---

## 7. Telemetry

The prototype uses network telemetry containing:

| Metric | Purpose |
|---|---|
| Latency | Measures network response delay |
| Packet Loss | Detects lost packets |
| CPU | Detects device processing stress |
| Memory | Monitors device resource usage |
| Bandwidth | Measures link utilization |
| Interface Errors | Detects possible interface/link problems |
| Traffic | Helps identify unusual traffic behavior |

The demonstration uses four network devices:

```text
R1
R2
R3
R4
```

---

## 8. Data Generation

A historical telemetry dataset was generated for model training.

The current prototype contains:

**4,000 historical records**

Example structure:

```text
device | latency | packet_loss | cpu | memory |
bandwidth | interface_errors | traffic
```

The historical dataset provides a baseline for machine-learning anomaly detection.

---

## 9. Anomaly Detection

The system uses two complementary approaches.

### 9.1 Rule-Based Detection

Engineering rules identify abnormal values and combinations.

Examples include:

- Elevated latency
- High packet loss
- High CPU utilization
- Very high CPU utilization
- Severe interface errors

Each device receives an anomaly score and severity.

Example:

```text
R2 | Score: 5 | Severity: CRITICAL
Reasons:
- Very high CPU utilization
- Severe interface errors
```

This approach is useful because the reason for an alert is directly explainable.

### 9.2 Machine Learning Detection

The system also uses **Isolation Forest** from Scikit-learn.

Isolation Forest is an unsupervised machine-learning method that identifies observations that are different from the normal baseline.

The model is trained using the generated historical telemetry dataset.

The trained model is saved as:

```text
network_anomaly_model.pkl
```

---

## 10. Root-Cause Analysis

Detecting an anomaly is not enough.

The system uses:

- Anomaly severity
- Individual telemetry evidence
- Network topology
- Neighbor relationships

to identify the probable root-cause device.

For example:

```text
R2 → R3 → R4
```

If R2 has strong local fault indicators and downstream devices show degradation, R2 can be ranked as the probable source.

Example result:

```text
Root Cause: R2
Affected Devices: R3, R4
Confidence: 85%
```

---

## 11. Security Assessment

The system separately evaluates whether an anomaly may have security significance.

Indicators include combinations such as:

- Unusually high traffic
- High CPU combined with high traffic
- Packet loss combined with unusually high traffic

The output can classify a device as:

```text
NORMAL
OPERATIONAL ANOMALY
SUSPICIOUS
POTENTIAL SECURITY EVENT
```

The security assessment is intentionally separate from the operational root-cause analysis.

---

## 12. Explainable Incident Report

The final stage combines the analysis into an incident report.

Example:

```text
Incident ID: INC-20260914221901
Severity: HIGH
Root Cause: R2
Affected Devices: R3, R4
Root Cause Confidence: 85%
Security Status: SUSPICIOUS
```

The report also provides reasons explaining why the root cause was selected.

This makes the system more useful than a simple alert dashboard.

---

## 13. Setup Instructions

### Step 1: Open the backend directory

```powershell
cd "C:\Users\DELL\Downloads\Network Intelligence System\backend"
```

### Step 2: Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell shows `(venv)` at the beginning of the command line, the environment is active.

### Step 3: Install dependencies

```powershell
python -m pip install fastapi uvicorn pandas numpy scikit-learn networkx joblib
```

### Step 4: Generate historical data

```powershell
python historical_data.py
```

Expected result:

```text
Historical dataset generated successfully.
Total records: 4000
```

### Step 5: Train the ML model

```powershell
python train_model.py
```

Expected result:

```text
Model training completed successfully.
Model saved as: network_anomaly_model.pkl
```

---

## 14. Testing the ML Model

Run:

```powershell
python test_ml.py
```

The system should display telemetry and Isolation Forest results such as:

```text
ISOLATION FOREST RESULTS

R1 | NORMAL
R2 | ANOMALY
R3 | NORMAL
R4 | NORMAL
```

The exact result can vary because the prototype telemetry is generated dynamically.

---

## 15. Complete Incident Test

Run:

```powershell
python test_incident.py
```

The demonstration follows:

```text
STEP 1: TELEMETRY GENERATED
        ↓
STEP 2: ANOMALY DETECTION
        ↓
STEP 3: ROOT CAUSE ANALYSIS
        ↓
STEP 4: SECURITY ASSESSMENT
        ↓
INCIDENT REPORT
```

Example:

```text
Root Cause: R2
Affected Devices: ['R3', 'R4']
Confidence: 85%
```

---

## 16. Start the Web Application

From the `backend` directory:

```powershell
python -m uvicorn app:app --reload
```

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

Open the dashboard:

```text
http://127.0.0.1:8000/dashboard
```

---

## 17. Demonstration Scenario

The main demonstration is:

### Normal Network

The network begins with normal telemetry.

### Failure Injection

A fault is introduced into the simulated network.

Typical symptoms can include:

- Increased latency
- Increased packet loss
- High CPU
- Severe interface errors

### Intelligent Analysis

The system identifies abnormal devices and analyzes their relationship.

### Root Cause

Example:

```text
Root Cause: R2
Affected Devices: R3, R4
Confidence: 85%
```

### Security Assessment

The system checks whether the telemetry also contains indicators of a potential security event.

### Incident Report

The final result summarizes:

- Incident severity
- Root cause
- Affected devices
- Confidence
- Security status
- Explanation

---

## 18. Test Cases

| Test Case | Expected Result |
|---|---|
| Normal network | Devices classified as NORMAL |
| Latency spike | Latency anomaly detected |
| Packet loss | Packet-loss anomaly detected |
| Cascading failure | Root cause and affected devices identified |
| Traffic anomaly | Security assessment triggered when indicators combine |
| Noisy telemetry | Avoid unnecessary alerts where values remain within expected range |
| ML anomaly test | Isolation Forest produces anomaly scores |

---

## 19. Design Decisions

### Why FastAPI?

FastAPI provides a lightweight way to expose the analysis pipeline through HTTP APIs and connect it to the dashboard.

### Why Isolation Forest?

The prototype does not require a large labelled dataset. Isolation Forest is suitable for unsupervised anomaly detection.

### Why NetworkX?

NetworkX makes it simple to represent network topology and analyze device relationships.

### Why combine rules and ML?

Machine learning can identify unusual patterns, while engineering rules provide clear explanations.

Therefore, the prototype uses a hybrid approach:

```text
Engineering Knowledge
        +
Machine Learning
        =
Explainable Network Intelligence
```

---

## 20. Results

The prototype successfully demonstrates:

- Network telemetry generation
- Historical data generation
- ML model training
- Anomaly detection
- Root-cause analysis
- Affected-device identification
- Security assessment
- Explainable incident reporting
- Web-based visualization

A representative incident produced:

```text
Root Cause: R2
Affected Devices: R3, R4
Confidence: 85%
```

---

## 21. Limitations

This is a prototype and has several limitations:

1. Network telemetry is simulated rather than collected from live devices.
2. The topology is small.
3. Security classification is based on heuristic indicators.
4. The ML model is trained on generated data.
5. Real-world networks contain more complex dependencies.
6. The current system does not automatically remediate incidents.

---

## 22. Future Improvements

Possible future improvements include:

- Real Cisco telemetry integration
- SNMP integration
- NetFlow integration
- Streaming telemetry
- Larger real-world datasets
- More advanced ML models
- Time-series anomaly detection
- Automated incident response
- Real-time alert notifications
- Improved security-event correlation
- Larger and dynamic network topology

---

## 23. Conclusion

The Network Intelligence System demonstrates a transition from traditional monitoring to intelligent network analysis.

Instead of simply saying:

```text
"Packet loss is high on R3."
```

the system attempts to answer:

```text
Why?
→ R2 is the probable root cause.

What is affected?
→ R3 and R4.

How confident are we?
→ 85%.

Could it be security-related?
→ Security assessment performed.

What should the administrator know?
→ An explainable incident report.
```

The prototype therefore demonstrates how network telemetry, engineering reasoning, machine learning, topology analysis, and security assessment can be combined into a single network intelligence workflow.
