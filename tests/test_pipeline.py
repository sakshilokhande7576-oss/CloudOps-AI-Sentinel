
import unittest

from detectors.log_analyzer import analyze_logs
from detectors.metrics_detector import analyze_metrics
from investigator.incident_investigator import (
    determine_severity,
    get_severity_reason,
    investigate_incidents,
)


class TestLogAnalyzer(unittest.TestCase):

    def test_missing_log_file_returns_warning(self):
        result = analyze_logs(
            "logs/this_file_does_not_exist.log"
        )

        self.assertEqual(result["errors"], [])
        self.assertEqual(result["severity"], "LOW")
        self.assertTrue(
            any(
                "Log file not found" in warning
                for warning in result["warnings"]
            )
        )


class TestMetricsDetector(unittest.TestCase):

    def test_high_cpu_and_memory(self):
        incidents = analyze_metrics(
            cpu_usage=82,
            memory_usage=91,
            disk_usage=65,
        )
        self.assertEqual(len(incidents), 2)

    def test_normal_metrics(self):
        incidents = analyze_metrics(
            cpu_usage=30,
            memory_usage=45,
            disk_usage=50,
        )
        self.assertEqual(incidents, [])


class TestIncidentSeverity(unittest.TestCase):

    def test_repeated_errors_are_high(self):
        severity = determine_severity(
            [
                "Database connection failed",
                "Database connection failed",
            ],
            [],
            [],
        )
        self.assertEqual(severity, "HIGH")

    def test_single_error_is_medium(self):
        severity = determine_severity(
            ["Database connection failed"],
            [],
            [],
        )
        self.assertEqual(severity, "MEDIUM")

    def test_multiple_metric_alerts_are_high(self):
        severity = determine_severity(
            [],
            [],
            ["High CPU", "High memory"],
        )
        self.assertEqual(severity, "HIGH")

    def test_multiple_warnings_are_medium(self):
        severity = determine_severity(
            [],
            ["CPU warning", "Memory warning"],
            [],
        )
        self.assertEqual(severity, "MEDIUM")

    def test_single_warning_is_low(self):
        severity = determine_severity(
            [],
            ["CPU warning"],
            [],
        )
        self.assertEqual(severity, "LOW")

    def test_no_incidents_are_low(self):
        severity = determine_severity([], [], [])
        self.assertEqual(severity, "LOW")


class TestSeverityReason(unittest.TestCase):

    def test_repeated_error_reason(self):
        reason = get_severity_reason(
            ["Database failed", "Database failed"],
            [],
            [],
        )
        self.assertIn("Repeated log errors", reason)

    def test_multiple_metric_alerts_reason(self):
        reason = get_severity_reason(
            [],
            [],
            ["High CPU", "High memory"],
        )
        self.assertIn("Multiple resource alerts", reason)

    def test_combined_error_and_metric_reason(self):
        reason = get_severity_reason(
            ["Database failed"],
            [],
            ["High CPU"],
        )
        self.assertIn("Log errors and resource alerts", reason)

    def test_no_incidents_reason(self):
        reason = get_severity_reason([], [], [])
        self.assertIn("No incidents detected", reason)


if __name__ == "__main__":
    unittest.main(verbosity=2)
