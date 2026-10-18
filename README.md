# CloudOps AI Sentinel



A local-first Python project for system resource monitoring, server log analysis, incident severity classification, and automated investigation recommendations.



## Overview



CloudOps AI Sentinel combines system metrics and server log analysis to identify potential operational issues and produce a structured incident report.



The project currently monitors the local Windows machine and analyzes sample server logs. It is designed as a foundation for future cloud operations monitoring.



## Features



\- \*\*System Metrics Monitoring:\*\* Collects CPU, memory, and disk usage using `psutil`.

\- \*\*Log Analysis:\*\* Detects error and warning events from server logs.

\- \*\*Incident Severity Engine:\*\* Classifies incidents as HIGH, MEDIUM, or LOW using configurable rules.

\- \*\*Severity Explanation:\*\* Explains why an incident received its severity level.

\- \*\*Investigation Recommendations:\*\* Generates suggested actions based on detected issues.

\- \*\*JSON Reporting:\*\* Saves findings, severity, system metrics, and recommendations.

\- \*\*Web Dashboard:\*\* Displays monitoring results using Flask.

\- \*\*Unit Testing:\*\* Tests metrics detection, severity classification, and severity explanations.



## Technology Stack



\- Python 3.11

\- Flask

\- psutil

\- unittest

\- HTML and CSS

\- JSON

\- Git and GitHub



## Project Architecture



```text

CloudOps-AI-Sentinel/

â”œâ”€â”€ app.py

â”œâ”€â”€ main.py

â”œâ”€â”€ detectors/

â”‚   â”œâ”€â”€ log\_analyzer.py

â”‚   â””â”€â”€ metrics\_detector.py

â”œâ”€â”€ investigator/

â”‚   â””â”€â”€ incident\_investigator.py

â”œâ”€â”€ logs/

â”‚   â””â”€â”€ server.log

â”œâ”€â”€ reports/

â”‚   â””â”€â”€ incident\_report.json

â”œâ”€â”€ templates/

â”‚   â””â”€â”€ dashboard.html

â””â”€â”€ tests/

&#x20;   â””â”€â”€ test\_pipeline.py

```



## How It Works



1\. Collects CPU, memory, and disk usage from the local computer.

2\. Reads the configured server log file.

3\. Detects log errors, warnings, and resource threshold violations.

4\. Determines the overall incident severity.

5\. Explains the severity and generates recommended actions.

6\. Saves the results as a JSON report and displays them on a Flask dashboard.



## Installation



Install Python 3.11, then install the dependencies:



```powershell

python -m pip install flask psutil

```



If `python` is not available in your Windows terminal, use the full path to your Python executable.



## Run the Dashboard



From the project root directory:



```powershell

python app.py

```



Open this address in your browser:



```text

http://127.0.0.1:5000

```



The dashboard runs locally on your computer.



## Run Tests



```powershell

python -m unittest discover -s tests -v

```



The current test suite contains 12 tests covering metrics detection, incident severity, and severity explanations.



## Current Limitations



\- Metrics are collected from the local Windows computer, not a remote cloud server.

\- The supplied server log is sample data and does not represent a live production server.

\- Severity classification uses predefined rules rather than a trained machine-learning model.

\- AWS services and remote infrastructure integrations are not currently connected.



## Future Improvements



\- Add monitoring for remote Linux servers.

\- Integrate AWS CloudWatch metrics and logs.

\- Add configurable alert thresholds.

\- Introduce incident history and trend analysis.

\- Explore agent-assisted investigation and root-cause analysis.



## Disclaimer



This project is intended for learning and portfolio demonstration. It is not yet a production-grade monitoring or incident-response platform.



## Author



\*\*Sakshi Lokhande\*\*



\- GitHub: https://github.com/sakshilokhande7576-oss

\- LinkedIn: https://linkedin.com/in/sakshi-lokhande-29b77825b
