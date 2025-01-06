import argparse
import json
import os
from datetime import datetime

# Severity order for sorting
SEVERITY_ORDER = {
    "critical": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
    "warning": 5,
    "unknown": 6,
    "n/a": 7,  # Ensure N/A (passed) shows last
}


def generate_html_report(input_file, summary_file, output_file, css_file=None, js_file=None):
    try:
        with open(input_file, "r") as file:
            report_data = json.load(file)

        with open(summary_file, "r") as file:
            summary_data = json.load(file)

        # Extract summary and linter data
        summary = report_data.get("summary", {})
        linters = report_data.get("linters", {})

        # Collect and sort all issues by severity
        all_issues = [
            issue
            for linter_issues in linters.values()
            for issue in linter_issues
            if issue.get("Severity", "").lower() != "n/a"
        ]
        sorted_issues = sorted(all_issues, key=lambda x: SEVERITY_ORDER.get(x.get("Severity", "").lower(), 99))

        # Start building the HTML content
        html = ["<!DOCTYPE html>", "<html>", "<head>", "<meta charset='UTF-8'>"]
        html.append("<title>AI Sec Report</title>")

        # Add optional CSS
        if css_file and os.path.exists(css_file):
            html.append(f'<link rel="stylesheet" href="{css_file}">')

        # Add optional JavaScript
        if js_file and os.path.exists(js_file):
            html.append(f'<script src="{js_file}"></script>')

        html.append("</head>")
        html.append("<body>")
        html.append("<h1>AI Sec Report</h1>")

        # Add linter filter
        html.append("""
        <div style="margin-bottom: 20px;">
            <label for="linter-filter">Filter by Linter:</label>
            <select id="linter-filter">
                <option value="">All</option>
                <option value="Checkov">Checkov</option>
                <option value="TFLint">TFLint</option>
                <option value="TFsec">TFsec</option>
            </select>
        </div>
        """)

        # Severity color mapping
        severity_colors = {
            "critical": "#f5c6cb",
            "high": "#ffe5b4",
            "medium": "#fff3cd",
            "low": "#d4edda",
            "warning": "#d1ecf1",
            "unknown": "#f0f0f0",
            "n/a": "#e8e8e8",
        }

        # Summary Section
        html.append("<h2>Issue Summary</h2>")
        html.append("<div class='summary-table' style='width: 50%; margin: 0 auto;'>")
        html.append("<table>")
        html.append("<thead><tr><th>Severity</th><th>Count</th></tr></thead>")
        html.append("<tbody>")

        for severity, count in summary_data.get("by_severity", {}).items():
            bg_color = severity_colors.get(severity.lower(), "#ffffff")
            html.append(
                f"<tr style='background-color: {bg_color};'><td>{severity.capitalize()}</td><td>{count}</td></tr>"
            )

        html.append("</tbody></table></div>")
        html.append(f"<p style='text-align: center;'><strong>Total Linters:</strong> {summary.get('linted_files', 0)}</p>")
        html.append(f"<p style='text-align: center;'><strong>Total Issues:</strong> {summary_data.get('total_issues', 0)}</p>")

        # Add spacing before Lint Issues section
        html.append("<div style='margin-top: 40px;'></div>")

        # Linter Issues Section
        html.append("<h2>Lint Issues (Sorted by Severity)</h2>")
        html.append("<div class='scrollable-table'>")
        html.append("<table>")
        html.append(
            "<thead><tr><th>LINTER</th><th>FILE</th><th>LINE</th><th>DESCRIPTION</th><th>SEVERITY</th>"
            "<th>CONTEXT</th><th>LINKS</th></tr></thead>"
        )
        html.append("<tbody>")

        for issue in sorted_issues:
            severity = issue.get("Severity", "").lower()

            bg_color = severity_colors.get(severity, "#ffffff")
            html.append(f"<tr style='background-color: {bg_color};'>")
            html.append(f"<td>{issue.get('Linter', 'N/A')}</td>")
            html.append(f"<td>{issue.get('File', 'N/A')}</td>")
            html.append(f"<td>{issue.get('Line', 'N/A')}</td>")
            html.append(f"<td>{issue.get('Description', 'N/A')}</td>")
            html.append(f"<td>{issue.get('Severity', 'N/A')}</td>")
            html.append(f"<td>{issue.get('Context', 'N/A')}</td>")

            # Process links
            if "Links" in issue:
                links = issue["Links"]
                if isinstance(links, list):
                    link_html = "<br>".join(f'<a href="{link}" target="_blank">{link}</a>' for link in links)
                else:
                    link_html = f'<a href="{links}" target="_blank">{links}</a>'
            else:
                link_html = ""
            html.append(f"<td>{link_html}</td>")
            html.append("</tr>")

        html.append("</tbody></table>")
        html.append("</div>")

        # Footer Section
        html.append("<footer>")
        html.append(f"Report generated on <strong>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</strong>")
        html.append("</footer>")

        html.append("</body></html>")

        # Write the HTML content to the output file
        with open(output_file, "w") as file:
            file.write("\n".join(html))

        print(f"HTML report generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating report: {e}")


# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a JSON report to an HTML report.")
    parser.add_argument("--input", required=True, help="Path to the input JSON report file.")
    parser.add_argument("--summary", required=True, help="Path to the summary JSON file.")
    parser.add_argument("--output", required=True, help="Path to the output HTML file.")
    parser.add_argument("--css", help="Path to the optional CSS file for styling.")
    parser.add_argument("--js", help="Path to the optional JavaScript file for interactivity.")

    args = parser.parse_args()
    generate_html_report(args.input, args.summary, args.output, args.css, args.js)