
from detectors.log_analyzer import analyze_logs
from detectors.metrics_detector import analyze_metrics
from investigator.incident_investigator import investigate_incidents
from reports.report_writer import save_incident_report


def main():
    print("\n========================================")
    print("       CLOUDOPS AI SENTINEL")
    print("========================================")

    # Step 1: Analyze server logs
    print("\n[1/3] Analyzing server logs...")

    log_results = analyze_logs("logs/server.log")

    # Step 2: Analyze system metrics
    print("\n[2/3] Analyzing system metrics...")

    metric_results = analyze_metrics(
        cpu_usage=82,
        memory_usage=91,
        disk_usage=65,
    )

    # Step 3: Investigate all detected incidents
    print("\n[3/3] Investigating incidents...")

    investigation = investigate_incidents(
        log_errors=log_results["errors"],
        log_warnings=log_results["warnings"],
        metric_incidents=metric_results,
    )

    # Step 4: Save the incident report
    save_incident_report(investigation)

    print("\n========================================")
    print("       ANALYSIS COMPLETED")
    print("========================================")


if __name__ == "__main__":
    main()
