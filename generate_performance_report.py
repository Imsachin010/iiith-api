import json
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def generate_performance_report():
    """Generate a performance report from Locust test results"""
    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "average_response_time": 0,
            "requests_per_second": 0
        },
        "endpoints": {
            "add": {"success_rate": 0, "avg_response_time": 0},
            "multiply": {"success_rate": 0, "avg_response_time": 0},
            "check_even_odd": {"success_rate": 0, "avg_response_time": 0}
        }
    }

    # Save report to file
    with open("performance_report.json", "w") as f:
        json.dump(report, f, indent=4)

    # Generate HTML report
    html_report = f"""
    <html>
    <head>
        <title>API Performance Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .summary {{ background-color: #f5f5f5; padding: 20px; border-radius: 5px; }}
            .endpoint {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; }}
            .success {{ color: green; }}
            .failure {{ color: red; }}
        </style>
    </head>
    <body>
        <h1>API Performance Report</h1>
        <p>Generated at: {report['timestamp']}</p>
        
        <div class="summary">
            <h2>Summary</h2>
            <p>Total Requests: {report['summary']['total_requests']}</p>
            <p>Successful Requests: {report['summary']['successful_requests']}</p>
            <p>Failed Requests: {report['summary']['failed_requests']}</p>
            <p>Average Response Time: {report['summary']['average_response_time']}ms</p>
            <p>Requests per Second: {report['summary']['requests_per_second']}</p>
        </div>

        <h2>Endpoint Performance</h2>
        <div class="endpoint">
            <h3>Add Numbers</h3>
            <p>Success Rate: {report['endpoints']['add']['success_rate']}%</p>
            <p>Average Response Time: {report['endpoints']['add']['avg_response_time']}ms</p>
        </div>
        <div class="endpoint">
            <h3>Multiply Numbers</h3>
            <p>Success Rate: {report['endpoints']['multiply']['success_rate']}%</p>
            <p>Average Response Time: {report['endpoints']['multiply']['avg_response_time']}ms</p>
        </div>
        <div class="endpoint">
            <h3>Check Even/Odd</h3>
            <p>Success Rate: {report['endpoints']['check_even_odd']['success_rate']}%</p>
            <p>Average Response Time: {report['endpoints']['check_even_odd']['avg_response_time']}ms</p>
        </div>
    </body>
    </html>
    """

    with open("performance_report.html", "w") as f:
        f.write(html_report)

if __name__ == "__main__":
    generate_performance_report() 