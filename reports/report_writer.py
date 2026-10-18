
import json
from datetime import datetime
from pathlib import Path


def save_incident_report(
    investigation,
    metrics=None,
    output_path="reports/incident_report.json",
):
    """Save incident findings, severity, metrics, and recommendations."""

    report = {
        "project": "CloudOps AI Sentinel",
        "generated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "severity": investigation["severity"],
        "severity_reason": investigation.get(
            "severity_reason",
            "No severity reason provided.",
        ),
        "system_metrics": metrics or {},
        "findings": investigation["findings"],
        "recommendations": investigation["recommendations"],
    }

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print(f"\nIncident report saved to: {path}")
    return str(path)
