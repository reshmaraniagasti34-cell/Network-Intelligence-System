# anomaly.py

def calculate_anomaly_score(device):
    """
    Calculate an anomaly score for one network device.

    Higher score = more abnormal behavior.
    """

    score = 0
    reasons = []

    # -----------------------------
    # 1. Latency
    # -----------------------------
    if device["latency"] > 80:
        score += 2
        reasons.append("High latency")

    elif device["latency"] > 50:
        score += 1
        reasons.append("Elevated latency")


    # -----------------------------
    # 2. Packet Loss
    # -----------------------------
    if device["packet_loss"] > 10:
        score += 3
        reasons.append("Severe packet loss")

    elif device["packet_loss"] > 5:
        score += 2
        reasons.append("High packet loss")

    elif device["packet_loss"] > 2:
        score += 1
        reasons.append("Elevated packet loss")


    # -----------------------------
    # 3. CPU utilization
    # -----------------------------
    if device["cpu"] > 85:
        score += 2
        reasons.append("Very high CPU utilization")

    elif device["cpu"] > 70:
        score += 1
        reasons.append("High CPU utilization")


    # -----------------------------
    # 4. Memory utilization
    # -----------------------------
    if device["memory"] > 90:
        score += 2
        reasons.append("Very high memory utilization")

    elif device["memory"] > 80:
        score += 1
        reasons.append("High memory utilization")


    # -----------------------------
    # 5. Interface errors
    # -----------------------------
    if device["interface_errors"] > 10:
        score += 3
        reasons.append("Severe interface errors")

    elif device["interface_errors"] > 5:
        score += 2
        reasons.append("High interface errors")

    elif device["interface_errors"] > 2:
        score += 1
        reasons.append("Elevated interface errors")


    # -----------------------------
    # Determine severity
    # -----------------------------
    if score >= 5:
        severity = "CRITICAL"

    elif score >= 2:
        severity = "WARNING"

    else:
        severity = "NORMAL"


    return {
        "device": device["device"],
        "anomaly_score": score,
        "severity": severity,
        "reasons": reasons
    }
