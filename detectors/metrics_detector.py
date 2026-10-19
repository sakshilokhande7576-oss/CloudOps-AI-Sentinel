import psutil
from pathlib import Path


def get_system_metrics():
    """Collect real CPU, memory, and disk usage from this computer."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage(Path.home().anchor).percent

    return {
        "cpu": cpu_usage,
        "memory": memory_usage,
        "disk": disk_usage,
    }


def analyze_metrics(cpu_usage, memory_usage, disk_usage):
    """Detect resource usage above configured thresholds."""
    incidents = []

    if cpu_usage >= 80:
        incidents.append(f"HIGH CPU usage detected: {cpu_usage}%")

    if memory_usage >= 85:
        incidents.append(f"HIGH memory usage detected: {memory_usage}%")

    if disk_usage >= 90:
        incidents.append(f"HIGH disk usage detected: {disk_usage}%")

    print("\n========== SYSTEM METRICS ANALYSIS ==========")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")

    if incidents:
        for incident in incidents:
            print("WARNING:", incident)
    else:
        print("System metrics are within configured thresholds.")

    return incidents


if __name__ == "__main__":
    metrics = get_system_metrics()
    analyze_metrics(
        cpu_usage=metrics["cpu"],
        memory_usage=metrics["memory"],
        disk_usage=metrics["disk"],
    )
