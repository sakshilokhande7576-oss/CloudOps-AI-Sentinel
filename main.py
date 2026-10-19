
from detectors.log_analyzer import analyze_logs
from detectors.metrics_detector import analyze_metrics
from investigator.incident_investigator import investigate_incidents
from reports.report_writer import save_incident_report


def main():
    print("\n========================================")
    print("       CLOUDOPS AI SENTINEL")
    print("========================================")

    print("\n[1/3] Analyzing server logs...")
    log_results = analyze_logs("logs/server.log")

    print("\n[2/3] Analyzing system metrics...")

    demo_metrics = {
        "cpu": 82,
        "memory": 91,
        "disk": 65,
    }

    metric_results = analyze_metrics(
        cpu_usage=demo_metrics["cpu"],
        memory_usage=demo_metrics["memory"],
        disk_usage=demo_metrics["disk"],
    )

    print("\n[3/3] Investigating incidents...")

    investigation = investigate_incidents(
        log_errors=log_results["errors"],
        log_warnings=log_results["warnings"],
        metric_incidents=metric_results,
    )

    save_incident_report(
        investigation,
        metrics=demo_metrics,
    )

    print("\n========================================")
    print("       ANALYSIS COMPLETED")
    print("========================================")


if __name__ == "__main__":
    main()
