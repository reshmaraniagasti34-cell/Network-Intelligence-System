from telemetry import generate_telemetry, set_failure
from anomaly import calculate_anomaly_score
from root_cause import analyze_root_cause
from security import assess_security
from incident import generate_incident_report


print("\n")
print("==============================================")
print("       NETWORK INTELLIGENCE SYSTEM")
print("       COMPLETE PIPELINE DEMONSTRATION")
print("==============================================")
print()


# =================================================
# STEP 1 — Generate telemetry
# =================================================

set_failure(True)

telemetry = generate_telemetry()


print("STEP 1: TELEMETRY GENERATED")
print("----------------------------------------------")

for device in telemetry:

    print(
        device["device"],
        "| Latency:", device["latency"],
        "| Packet Loss:", device["packet_loss"],
        "| CPU:", device["cpu"],
        "| Traffic:", device["traffic"],
        "| Interface Errors:",
        device["interface_errors"]
    )


# =================================================
# STEP 2 — Anomaly Detection
# =================================================

anomaly_results = []

for device in telemetry:

    result = calculate_anomaly_score(device)

    anomaly_results.append(result)


print("\n")
print("STEP 2: ANOMALY DETECTION")
print("----------------------------------------------")

for result in anomaly_results:

    print(
        result["device"],
        "| Score:", result["anomaly_score"],
        "| Severity:", result["severity"],
        "| Reasons:",
        result["reasons"]
    )


# =================================================
# STEP 3 — Root Cause Analysis
# =================================================

root_cause_result = analyze_root_cause(
    anomaly_results
)


print("\n")
print("STEP 3: ROOT CAUSE ANALYSIS")
print("----------------------------------------------")

print(
    "Root Cause:",
    root_cause_result["root_cause"]
)

print(
    "Affected Devices:",
    root_cause_result["affected_devices"]
)

print(
    "Confidence:",
    str(root_cause_result["confidence"]) + "%"
)


# =================================================
# STEP 4 — Security Assessment
# =================================================

security_results = []

for device in telemetry:

    result = assess_security(device)

    security_results.append(result)


print("\n")
print("STEP 4: SECURITY ASSESSMENT")
print("----------------------------------------------")

for result in security_results:

    print(
        result["device"],
        "| Classification:",
        result["classification"],
        "| Score:",
        result["security_score"]
    )


# =================================================
# STEP 5 — Incident Report
# =================================================

report = generate_incident_report(
    telemetry,
    anomaly_results,
    root_cause_result,
    security_results
)


print("\n")
print("==============================================")
print("             INCIDENT REPORT")
print("==============================================")

print(
    "Incident ID:",
    report["incident_id"]
)

print(
    "Severity:",
    report["severity"]
)

print(
    "Root Cause:",
    report["root_cause"]
)

print(
    "Affected Devices:",
    report["affected_devices"]
)

print(
    "Root Cause Confidence:",
    str(report["root_cause_confidence"])
    + "%"
)

print(
    "Security Status:",
    report["security_status"]
)

print("\nExplanation:")

for explanation in report["explanation"]:

    print("-", explanation)

print("==============================================")
