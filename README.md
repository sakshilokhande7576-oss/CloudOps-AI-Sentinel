# CloudOps AI Sentinel

**Local System Monitoring | Log Analysis | Incident Severity | Flask Dashboard**

CloudOps AI Sentinel is a Python-based monitoring and incident investigation project that analyzes system resource usage and server log events to identify operational issues and generate actionable recommendations.

## Overview

The project currently monitors the local Windows computer and analyzes sample server logs. It combines resource metrics, log analysis, rule-based severity classification, and investigation recommendations in a web dashboard and structured JSON report.

The project is designed as a foundation for future cloud operations monitoring.

## Features

- **System Monitoring:** Collects CPU, memory, and disk usage using `psutil`.
- **Log Analysis:** Detects error and warning events from server logs.
- **Incident Severity Engine:** Classifies incidents as HIGH, MEDIUM, or LOW using predefined rules.
- **Severity Explanations:** Provides reasons for incident classifications.
- **Investigation Recommendations:** Suggests actions based on detected issues.
- **JSON Reporting:** Generates structured incident reports.
- **Web Dashboard:** Displays system metrics, findings, severity, and recommendations using Flask.
- **Unit Testing:** Tests metrics detection, severity classification, and severity explanations.

## Technology Stack

- Python 3.11
- Flask
- psutil
- unittest
- HTML and CSS
- JSON
- Git and GitHub

## Architecture

```text
CloudOps-AI-Sentinel/
├── app.py
├── main.py
├── detectors/
│   ├── log_analyzer.py
│   └── metrics_detector.py
├── investigator/
│   └── incident_investigator.py
├── logs/
│   └── server.log
├── reports/
├── templates/
│   └── dashboard.html
└── tests/
    └── test_pipeline.py
```

The incident report is generated locally when the application runs.

## How It Works

1. Collects CPU, memory, and disk usage from the local computer.
2. Reads the configured server log file.
3. Detects log errors, warnings, and resource threshold violations.
4. Calculates incident severity using predefined rules.
5. Generates severity explanations and recommended actions.
6. Produces a JSON incident report and displays results on the Flask dashboard.

## Getting Started

### Prerequisites

- Python 3.11
- pip
- Git (optional, for cloning the repository)

### Install Dependencies

From the project root directory, run:

```powershell
python -m pip install flask psutil
```

If Python is not available through the `python` command on Windows, use the full path to your Python executable.

### Run the Dashboard

```powershell
python app.py
```

Open the dashboard in your browser:

http://127.0.0.1:5000/

Keep the terminal open while using the dashboard. Press `Ctrl + C` in the terminal to stop the server.

### Run Unit Tests

```powershell
python -m unittest discover -s tests -v
```

The current test suite contains 12 tests covering metrics detection, incident severity, and severity explanations.

## Current Scope and Limitations

- System metrics are collected from the local Windows computer.
- Log analysis uses the project's sample server log file.
- Severity classification uses predefined rules, not a trained machine-learning model.
- Investigation recommendations are rule-based; a fully autonomous agentic investigation workflow is not yet implemented.
- Remote Linux servers and AWS services are not currently connected.
- The project is intended for learning and portfolio demonstration, not production incident response.

## Future Enhancements

- Integrate remote Linux server monitoring.
- Explore AWS CloudWatch metrics and log integration.
- Add configurable monitoring thresholds.
- Maintain incident history and trend analysis.
- Develop agent-assisted investigation and root-cause analysis.

## Author

**Sakshi Lokhande**

- GitHub: https://github.com/sakshilokhande7576-oss
- LinkedIn: https://linkedin.com/in/sakshi-lokhande-29b77825b