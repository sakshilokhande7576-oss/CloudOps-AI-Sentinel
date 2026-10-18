
from collections import Counter


def determine_severity(log_errors, log_warnings, metric_incidents):
    """Determine severity using clear incident rules."""

    error_counts = Counter(log_errors)
    repeated_errors = any(count >= 2 for count in error_counts.values())

    if repeated_errors or len(metric_incidents) >= 2:
        return "HIGH"

    if log_errors or metric_incidents or len(log_warnings) >= 2:
        return "MEDIUM"

    return "LOW"


def get_severity_reason(log_errors, log_warnings, metric_incidents):
    """Explain the actual reason behind the incident severity."""

    error_counts = Counter(log_errors)
    repeated_errors = any(count >= 2 for count in error_counts.values())
    multiple_metric_alerts = len(metric_incidents) >= 2

    if repeated_errors and multiple_metric_alerts:
        return (
            "Repeated log errors and multiple resource alerts "
            "require priority investigation."
        )

    if repeated_errors:
        return (
            "Repeated log errors detected; investigate the recurring "
            "error and its underlying cause."
        )

    if multiple_metric_alerts:
        return (
            "Multiple resource alerts detected; investigate system "
            "resource usage."
        )

    if log_errors and metric_incidents:
        return (
            "Log errors and resource alerts detected; investigate "
            "both application and system health."
        )

    if log_errors:
        return "Log errors detected; inspect the affected application."

    if metric_incidents:
        return "Resource threshold exceeded; review system health."

    if len(log_warnings) >= 2:
        return "Multiple log warnings detected; review them for escalation."

    if log_warnings:
        return "A log warning was detected; continue monitoring."

    return "No incidents detected; continue routine monitoring."


def investigate_incidents(log_errors, log_warnings, metric_incidents):
    """Combine log and resource findings into an investigation report."""

    findings = []
    recommendations = []
    error_counts = Counter(log_errors)

    if log_errors:
        findings.append(
            f"{len(log_errors)} error event(s) found in server logs."
        )
        recommendations.append(
            "Inspect application logs and verify affected services."
        )

    for message, count in error_counts.items():
        if count >= 2:
            findings.append(
                f"Repeated error: '{message}' occurred {count} times."
            )
            recommendations.append(
                "Investigate the recurring error and check its underlying cause."
            )

    if log_warnings:
        findings.append(
            f"{len(log_warnings)} warning event(s) found in server logs."
        )
        recommendations.append(
            "Review warnings and monitor whether they become errors."
        )

    if metric_incidents:
        findings.append(
            f"{len(metric_incidents)} resource metric alert(s) detected."
        )
        recommendations.extend(metric_incidents)
        recommendations.append(
            "Check CPU, memory, and disk usage before restarting services."
        )

    severity = determine_severity(
        log_errors,
        log_warnings,
        metric_incidents,
    )

    severity_reason = get_severity_reason(
        log_errors,
        log_warnings,
        metric_incidents,
    )

    if not findings:
        findings.append("No incidents detected.")

    if not recommendations:
        recommendations.append("Continue routine monitoring.")

    print("\n========== INCIDENT INVESTIGATION ==========")
    print(f"Overall Severity: {severity}")
    print(f"Severity Reason: {severity_reason}")

    print("\nFindings:")
    for finding in findings:
        print(f"- {finding}")

    print("\nRecommended Actions:")
    for recommendation in recommendations:
        print(f"- {recommendation}")

    return {
        "severity": severity,
        "severity_reason": severity_reason,
        "findings": findings,
        "recommendations": recommendations,
    }


if __name__ == "__main__":
    investigate_incidents(
        log_errors=[
            "Database connection failed",
            "Database connection failed",
        ],
        log_warnings=[
            "CPU usage reached 82%",
            "Memory usage reached 91%",
        ],
        metric_incidents=[],
    )
