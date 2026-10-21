
from collections import Counter
from pathlib import Path


def analyze_logs(file_path):
    errors = []
    warnings = []

    log_path = Path(file_path)

    # Handle a missing log file safely
    if not log_path.is_file():
        print(f"WARNING: Log file not found: {log_path}")
        return {
            "errors": [],
            "warnings": [f"Log file not found: {log_path}"],
            "severity": "LOW",
            "unique_error_types": 0,
        }

    # Read log entries
    with log_path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if "ERROR" in line:
                errors.append(line.split("ERROR", 1)[1].strip())
            elif "WARNING" in line:
                warnings.append(line.split("WARNING", 1)[1].strip())

    # Count repeated errors
    error_counts = Counter(errors)

    # Determine log severity
    if any(count > 1 for count in error_counts.values()):
        severity = "HIGH"
    elif errors:
        severity = "MEDIUM"
    elif warnings:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    print("\n========== LOG ANALYSIS ==========")
    print(f"Total Errors: {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")
    print(f"Unique Error Types: {len(error_counts)}")
    print(f"Incident Severity: {severity}")

    print("\n========== REPEATED ERRORS ==========")
    repeated_found = False

    for message, count in error_counts.items():
        if count > 1:
            repeated_found = True
            print(f"{message} (occurred {count} times)")

    if not repeated_found:
        print("No repeated errors detected.")

    print("\n========== WARNINGS ==========")
    if warnings:
        for message in warnings:
            print(message)
    else:
        print("No warnings detected.")

    return {
        "errors": errors,
        "warnings": warnings,
        "severity": severity,
        "unique_error_types": len(error_counts),
    }


if __name__ == "__main__":
    analyze_logs("logs/server.log")
