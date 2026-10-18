
from flask import Flask, render_template
from pathlib import Path
import json

from detectors.log_analyzer import analyze_logs
from detectors.metrics_detector import (
    analyze_metrics,
    get_system_metrics,
)
from investigator.incident_investigator import investigate_incidents
from reports.report_writer import save_incident_report

app = Flask(__name__)


def collect_report():
    """Collect local system metrics and analyze server logs."""

    print("\n========== CLOUDOPS AI SENTINEL ==========")

    # Step 1: Analyze server logs
    log_results = analyze_logs("logs/server.log")

    # Step 2: Collect actual metrics from this computer
    metrics = get_system_metrics()

    metric_incidents = analyze_metrics(
        cpu_usage=metrics["cpu"],
        memory_usage=metrics["memory"],
        disk_usage=metrics["disk"],
    )

    # Step 3: Investigate all detected incidents
    investigation = investigate_incidents(
        log_errors=log_results["errors"],
        log_warnings=log_results["warnings"],
        metric_incidents=metric_incidents,
    )

    # Step 4: Save investigation and actual system metrics
    save_incident_report(
        investigation,
        metrics=metrics,
    )

    return {
        "severity": investigation["severity"],
        "severity_reason": investigation["severity_reason"],
        "errors": log_results["errors"],
        "warnings": log_results["warnings"],
        "metrics": metrics,
        "metric_incidents": metric_incidents,
        "findings": investigation["findings"],
        "recommendations": investigation["recommendations"],
    }


@app.route("/")
def dashboard():
    report = collect_report()
    return render_template("dashboard.html", report=report)


@app.route("/api/report")
def api_report():
    # Generate a fresh report before returning the JSON.
    collect_report()

    report_path = Path("reports/incident_report.json")

    with report_path.open("r", encoding="utf-8") as file:
        return app.response_class(
            response=json.dumps(
                json.load(file),
                indent=4,
                ensure_ascii=False,
            ),
            status=200,
            mimetype="application/json",
        )


if __name__ == "__main__":
    app.run(debug=True)
