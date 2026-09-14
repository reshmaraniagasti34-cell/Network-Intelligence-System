# root_cause.py

from topology import create_network


def analyze_root_cause(anomaly_results):

    network = create_network()

    # Devices that have anomalies
    anomalous_devices = [
        result
        for result in anomaly_results
        if result["severity"] != "NORMAL"
    ]

    if not anomalous_devices:
        return {
            "root_cause": None,
            "affected_devices": [],
            "confidence": 0,
            "explanation": "No anomaly detected."
        }

    # ---------------------------------------
    # Calculate root cause score
    # ---------------------------------------

    candidates = []

    for result in anomalous_devices:

        device = result["device"]

        score = 0
        reasons = []

        # Interface errors are strong evidence
        if "Severe interface errors" in result["reasons"]:
            score += 5
            reasons.append(
                "Severe interface errors indicate a possible local link/interface fault"
            )

        # High CPU can indicate device stress
        if "High CPU utilization" in result["reasons"]:
            score += 2
            reasons.append(
                "High CPU utilization indicates device stress"
            )

        # Packet loss may be an effect of another fault
        if "Severe packet loss" in result["reasons"]:
            score += 1
            reasons.append(
                "Packet loss may be a downstream symptom"
            )

        # High latency can also be downstream
        if "High latency" in result["reasons"] or \
           "Elevated latency" in result["reasons"]:

            score += 1

            reasons.append(
                "Latency may be a downstream effect"
            )

        # ---------------------------------------
        # Connectivity influence
        # ---------------------------------------

        neighbors = list(network.neighbors(device))

        score += len(neighbors) * 0.5

        candidates.append({
            "device": device,
            "score": score,
            "reasons": reasons,
            "neighbors": neighbors
        })

    # Highest scoring device
    candidates.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    root = candidates[0]

    # Remaining anomalous devices
    affected_devices = [
        result["device"]
        for result in anomalous_devices
        if result["device"] != root["device"]
    ]

    # ---------------------------------------
    # Confidence
    # ---------------------------------------

    if len(candidates) == 1:
        confidence = 95

    elif len(candidates) > 1:

        second_score = candidates[1]["score"]

        if root["score"] > second_score:
            confidence = 85
        else:
            confidence = 60

    else:
        confidence = 0

    return {
        "root_cause": root["device"],
        "root_cause_score": root["score"],
        "affected_devices": affected_devices,
        "confidence": confidence,
        "explanation": root["reasons"],
        "candidates": candidates
    }
