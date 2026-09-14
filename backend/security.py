# security.py


def assess_security(device):
    """
    Determine whether a network anomaly looks operational
    or potentially security-related.
    """

    security_score = 0
    reasons = []

    # ---------------------------------------
    # 1. Sudden / unusually high traffic
    # ---------------------------------------

    if device["traffic"] > 90:

        security_score += 3

        reasons.append(
            "Unusually high traffic volume"
        )

    elif device["traffic"] > 80:

        security_score += 1

        reasons.append(
            "Elevated traffic volume"
        )


    # ---------------------------------------
    # 2. High CPU + high traffic
    # ---------------------------------------

    if device["cpu"] > 80 and device["traffic"] > 80:

        security_score += 3

        reasons.append(
            "High CPU combined with high traffic"
        )


    # ---------------------------------------
    # 3. Packet loss + high traffic
    # ---------------------------------------

    if device["packet_loss"] > 5 and device["traffic"] > 80:

        security_score += 3

        reasons.append(
            "Packet loss combined with unusually high traffic"
        )


    # ---------------------------------------
    # Determine classification
    # ---------------------------------------

    if security_score >= 5:

        classification = "POTENTIAL SECURITY EVENT"


    elif security_score >= 2:

        classification = "SUSPICIOUS"

    else:

        classification = "NORMAL"

    # ---------------------------------------
    # Confidence
    # ---------------------------------------

    if security_score >= 5:

        confidence = 85

    elif security_score >= 2:

        confidence = 65

    else:

        confidence = 100


    return {
        "device": device["device"],
        "security_score": security_score,
        "classification": classification,
        "confidence": confidence,
        "reasons": reasons
    }
