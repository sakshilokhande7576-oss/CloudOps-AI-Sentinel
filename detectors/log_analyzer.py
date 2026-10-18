
from collections import Counter


def analyze_logs(file_path):
    errors = []
    warnings = []

    # Read log entries
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if "ERROR" in line:
                errors.append(line.split("ERROR", 1)[1].strip())

            elif "WARNING" in line:
                warnings.append(line.split("WARNING", 1)[1].strip())

    # Count repeated errors
    error_counts = Counter(errors)

    # Determine severity
    if any(count > 1 for count in error_counts.values()):
        severity = "HIGH"
    elif errors or warnings:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    # Print analysis report
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

    # Return results so main.py can use them
    return {
        "errors": errors,
        "warnings": warnings,
        "severity": severity,
        "unique_error_types": len(error_counts),
    }


if __name__ == "__main__":
    analyze_logs("logs/server.log")
