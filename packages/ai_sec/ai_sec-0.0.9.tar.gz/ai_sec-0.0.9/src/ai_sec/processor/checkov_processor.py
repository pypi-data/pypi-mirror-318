import os
from typing import Dict, List

from ai_sec.models.checkov_model import CheckovIssue
from ai_sec.processor.ai_processor import AIProcessor  # Import the AIProcessor
from ai_sec.processor.lint_processor import LinterProcessor


class CheckovProcessor(LinterProcessor):
    def __init__(self, framework: str):
        """
        Initialize CheckovProcessor and AIProcessor with the provided framework.
        :param framework: The infrastructure framework being scanned (e.g., 'Terraform', 'CloudFormation').
        """
        super().__init__(framework=framework)
        # Initialize AIProcessor with the provided framework if the OpenAI API key is set
        self.ai_processor = (
            AIProcessor(framework=self.framework)
            if os.getenv("OPENAI_API_KEY")
            else None
        )

        # Variables to store pass/fail summary
        self.total_issues = 0  # Total issues (failed checks only)
        self.total_checks = 0  # Total checks (passed + failed)
        self.passed_issues = 0
        self.failed_issues = 0
        self.pass_percentage = 0.0

    def process_data(self, linter_results: Dict) -> List[Dict]:
        """
        Process Checkov results and append AI-generated severity/context for issues.
        Only failed issues are counted towards 'total_issues', but passed checks are tracked for pass percentage.
        """
        data = []

        # Process failed checks (considered as total issues)
        for issue in linter_results.get("failed_checks", []):
            self.failed_issues += 1  # Increment failed issues count
            checkov_issue = CheckovIssue(
                check_id=issue.get("check_id"),
                message=issue.get("message"),
                result=issue.get("result", "FAILED"),
                file_path=issue.get("file_path"),
                line_number_start=issue.get("line_number_start"),
                line_number_end=issue.get("line_number_end"),
                severity=issue.get("severity"),
                guideline=issue.get("guideline"),
                resource=issue.get("resource"),  # Include resource for additional context
            )

            issue_data = {
                "Linter": "Checkov",
                "File": checkov_issue.file_path,
                "Line": checkov_issue.line_range,  # Use line_range property for start - end
                "Description": checkov_issue.message,
                "Severity": checkov_issue.severity.upper() if checkov_issue.severity else "UNKNOWN",
                "Context": "",  # Context to be updated by AIProcessor if applicable
                "Links": ", ".join(checkov_issue.guideline or [])
                if isinstance(checkov_issue.guideline, list)
                else checkov_issue.guideline or "",
                "Additional Context": checkov_issue.resource or "",
            }

            # Use AIProcessor to update severity and context if available
            if self.ai_processor:
                issue_data = self.ai_processor.process_linter_issue(issue_data)

            # Append the processed issue to the data list
            data.append(issue_data)

        # Process passed checks (tracked for pass percentage but excluded from 'total_issues')
        for issue in linter_results.get("passed_checks", []):
            self.passed_issues += 1  # Increment passed issues count
            checkov_issue = CheckovIssue(
                check_id=issue.get("check_id"),
                message=issue.get("message"),
                result="PASSED",
                file_path=issue.get("file_path"),
                line_number_start=issue.get("line_number_start"),
                line_number_end=issue.get("line_number_end"),
                severity="N/A",
                guideline=issue.get("guideline"),
                resource=issue.get("resource"),
            )

            issue_data = {
                "Linter": "Checkov",
                "File": checkov_issue.file_path,
                "Line": checkov_issue.line_range,
                "Description": checkov_issue.message,
                "Severity": "N/A",
                "Context": "PASSED",
                "Links": ", ".join(checkov_issue.guideline or [])
                if isinstance(checkov_issue.guideline, list)
                else checkov_issue.guideline or "",
                "Additional Context": checkov_issue.resource or "",
            }

            # Append passed check data to maintain consistency but excluded from failed total
            data.append(issue_data)

        # Process parsing errors (considered as failed with unknown severity)
        for file in linter_results.get("parsing_errors", []):
            parsing_error_data = {
                "Linter": "Checkov",
                "File": file,
                "Line": None,
                "Description": "Parsing error occurred",
                "Severity": "UNKNOWN",
                "Context": "Parsing error",
                "Links": "",
                "Additional Context": "",
            }
            data.append(parsing_error_data)
            self.failed_issues += 1  # Count parsing errors as failed checks

        # Calculate totals
        self.total_issues = self.failed_issues  # Only failed checks count as total issues
        self.total_checks = self.failed_issues + self.passed_issues  # Total checks (passed + failed)
        if self.total_checks > 0:
            self.pass_percentage = (self.passed_issues / self.total_checks) * 100

        return data

    def get_summary(self) -> Dict:
        """Get the summary of pass/fail issues and the pass percentage."""
        return {
            "total_issues": self.total_issues,  # Only failed checks
            "passed_issues": self.passed_issues,
            "failed_issues": self.failed_issues,
            "pass_percentage": self.pass_percentage,
            "total_checks": self.total_checks,  # Total passed + failed checks for context
        }