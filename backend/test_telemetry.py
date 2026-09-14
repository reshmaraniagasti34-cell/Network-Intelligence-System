from telemetry import generate_telemetry, set_failure


print("\n========== NORMAL NETWORK ==========\n")

normal_data = generate_telemetry()

for device in normal_data:
    print(device)


print("\n========== INJECTING FAILURE ==========\n")

set_failure(True)

failure_data = generate_telemetry()

for device in failure_data:
    print(device)
