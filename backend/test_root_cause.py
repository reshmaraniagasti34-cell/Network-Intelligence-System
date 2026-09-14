# test_root_cause.py

from telemetry import generate_telemetry, set_failure
from anomaly import calculate_anomaly_score
from root_cause import analyze_root_cause


print("\n================================")
print(" ROOT CAUSE ANALYSIS TEST")
print("================================\n")


# Enable failure
set_failure(True)

telemetry = generate_telemetry()


# Detect anomalies
anomaly_results = []

for device in telemetry:

    result = calculate_anomaly_score(device)

    anomaly_results.append(result)


# Analyze root cause
analysis = analyze_root_cause(anomaly_results)


print("ROOT CAUSE:")
print(analysis["root_cause"])


print("\nAFFECTED DEVICES:")
print(analysis["affected_devices"])


print("\nCONFIDENCE:")
print(str(analysis["confidence"]) + "%")


print("\nEXPLANATION:")

for reason in analysis["explanation"]:

    print("-", reason)


print("\nCANDIDATE ANALYSIS:")

for candidate in analysis["candidates"]:

    print(
        candidate["device"],
        "Score:",
        candidate["score"],
        "Neighbors:",
        candidate["neighbors"]
    )
