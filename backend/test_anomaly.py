from telemetry import generate_telemetry, set_failure
from anomaly import calculate_anomaly_score


# Generate normal network
print("\n========== NORMAL NETWORK ==========\n")

set_failure(False)

normal_data = generate_telemetry()

for device in normal_data:

    result = calculate_anomaly_score(device)

    print(result)


# Generate failure
print("\n========== FAILURE NETWORK ==========\n")

set_failure(True)

failure_data = generate_telemetry()

for device in failure_data:

    result = calculate_anomaly_score(device)

    print(result)
