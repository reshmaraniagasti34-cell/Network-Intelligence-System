import random
import pandas as pd


DEVICES = ["R1", "R2", "R3", "R4"]


def generate_historical_data(samples=1000):

    records = []

    for _ in range(samples):

        for device in DEVICES:

            record = {

                "device": device,

                "latency": random.uniform(15, 35),

                "packet_loss": random.uniform(0, 1),

                "cpu": random.uniform(30, 60),

                "memory": random.uniform(40, 70),

                "bandwidth": random.uniform(30, 70),

                "interface_errors": random.randint(0, 2),

                "traffic": random.uniform(40, 100)
            }

            records.append(record)

    return pd.DataFrame(records)


if __name__ == "__main__":

    data = generate_historical_data()

    data.to_csv(
        "../data/historical_telemetry.csv",
        index=False
    )

    print("Historical dataset generated successfully.")

    print("Total records:", len(data))

    print("\nFirst 5 records:")

    print(data.head())
