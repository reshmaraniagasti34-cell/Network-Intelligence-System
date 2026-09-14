# incident.py

from datetime import datetime


def generate_incident_report(
    telemetry,
    anomaly_results,
    root_cause_result,
    security_results
):
    """
    Combine all analysis results into one explainable
    network incident report.
    """

    # -----------------------------------------
    # Find anomalous devices
    # -----------------------------------------

    anomalous_devices = [
        result
        for result in anomaly_results
        if result["severity"] != "NORMAL"
    ]

    # -----------------------------------------
    # Determine overall severity
    # -----------------------------------------

    if any(
        result["severity"] == "CRITICAL"
        for result in anomaly_results
    ):

        overall_severity = "CRITICAL"

    elif anomalous_devices:

        overall_severity = "HIGH"

    else:

        overall_severity = "NORMAL"


    # -----------------------------------------
    # Security classification
    # -----------------------------------------

    security_events = [
        result
        for result in security_results
        if result["classification"] == "POTENTIAL SECURITY EVENT"
    ]

    suspicious_events = [
        result
        for result in security_results
        if result["classification"] == "SUSPICIOUS"
    ]


    if security_events:

        security_status = "POTENTIAL SECURITY EVENT"

    elif suspicious_events:

        security_status = "SUSPICIOUS"

    else:

        security_status = "OPERATIONAL"


    # -----------------------------------------
    # Root cause
    # -----------------------------------------

    root_cause = root_cause_result.get(
        "root_cause"
    )

    affected_devices = root_cause_result.get(
        "affected_devices",
        []
    )

    confidence = root_cause_result.get(
        "confidence",
        0
    )


    # -----------------------------------------
    # Generate explanation
    # -----------------------------------------

    explanation = []

    if root_cause:

        explanation.append(
            f"{root_cause} is identified as the "
            f"probable root cause based on its "
            f"strong anomaly indicators and network "
            f"position."
        )


    if affected_devices:

        explanation.append(
            "Affected devices: "
            + ", ".join(affected_devices)
            + "."
        )


    # Add anomaly evidence

    for result in anomalous_devices:

        explanation.append(
            f"{result['device']} shows "
            + ", ".join(result["reasons"])
            + "."
        )


    # Add security evidence

    for result in security_events:

        explanation.append(
            f"{result['device']} shows indicators "
            f"consistent with a potential security event: "
            + ", ".join(result["reasons"])
            + "."
        )


    # -----------------------------------------
    # Create incident ID
    # -----------------------------------------

    incident_id = (
        "INC-"
        + datetime.now().strftime("%Y%m%d%H%M%S")
    )


    # -----------------------------------------
    # Final report
    # -----------------------------------------

    report = {

        "incident_id": incident_id,

        "timestamp": datetime.now().isoformat(),

        "severity": overall_severity,

        "root_cause": root_cause,

        "affected_devices": affected_devices,

        "root_cause_confidence": confidence,

        "security_status": security_status,

        "anomalous_devices": anomalous_devices,

        "explanation": explanation

    }


    return report
