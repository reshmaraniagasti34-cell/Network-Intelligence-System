import random
from datetime import datetime


# Network devices in our simulated network
DEVICES = ["R1", "R2", "R3", "R4"]


# This variable controls whether a failure is active
failure_mode = False


def set_failure(value: bool):
    """
    Enable or disable the simulated network failure.
    """
    global failure_mode
    failure_mode = value


def generate_telemetry():
    """
    Generate telemetry data for all network devices.
    """

    telemetry = []

    for device in DEVICES:

        # Normal network behavior
        data = {
            "timestamp": datetime.now().isoformat(),
            "device": device,

            "latency": round(
                random.uniform(15, 35), 2
            ),

            "packet_loss": round(
                random.uniform(0, 1), 2
            ),

            "cpu": round(
                random.uniform(30, 60), 2
            ),

            "memory": round(
                random.uniform(40, 70), 2
            ),

            "bandwidth": round(
                random.uniform(30, 70), 2
            ),

            "interface_errors": random.randint(
                0, 2
            ),

            "traffic": round(
                random.uniform(40, 100), 2
            )
        }


        # Simulated failure
        if failure_mode:

            # Root-cause device
            if device == "R2":

                data["interface_errors"] = random.randint(
                    15, 30
                )

                data["cpu"] = round(
                    random.uniform(70, 90), 2
                )


            # First affected device
            elif device == "R3":

                data["packet_loss"] = round(
                    random.uniform(8, 15), 2
                )

                data["latency"] = round(
                    random.uniform(70, 120), 2
                )


            # Second affected device
            elif device == "R4":

                data["latency"] = round(
                    random.uniform(60, 100), 2
                )


        telemetry.append(data)


    return telemetry
