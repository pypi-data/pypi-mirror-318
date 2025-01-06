# AI_Sec

AI_Sec is a powerful command-line tool for linting, security scanning, and reporting on infrastructure-as-code (IaC) such as Terraform and CloudFormation. It supports a variety of linters and security checkers, making it an essential tool for maintaining high-quality infrastructure code, with a focus on best practices and security.

## Table of Contents

- [Motivation](#motivation)
- [Python Versions](#python-versions)
- [Features](#features)
- [Installation](#installation)
  - [Option 1: Using a Virtual Environment and Symbolic Links](#option-1-using-a-virtual-environment-and-symbolic-links)
  - [Option 2: Installing Directly to System Python](#option-2-installing-directly-to-system-python)
- [Setting Up](#setting-up)
- [Commands](#commands)
- [Sample Configuration](#sample-configuration)
- [Contact](#contact)

## Motivation

Managing infrastructure code in a secure and scalable way is essential, especially with the rise of cloud-native technologies. AI_Sec was developed to automate the process of ensuring that your infrastructure code adheres to best practices by utilizing various linters and security scanners, generating detailed reports to highlight issues.

AI_Sec ensures that your infrastructure is both secure and follows the necessary guidelines by default using **Checkov**, while also supporting other popular linters such as **TFLint** and **TFSec**. The tool is designed to work with IaC frameworks like **Terraform** and **CloudFormation**, giving you comprehensive coverage.

## Python Versions

This project supports Python versions specified in the `pyproject.toml` file:

```toml
[tool.poetry.dependencies]
python = ">=3.10,<4.0"
```

## Features

- **Lint Terraform and CloudFormation Code**: Support for Checkov by default, with optional support for TFLint (v0.53.0) and TFSec (v1.28.0).
- **Security Scanning**: Detect vulnerabilities in your infrastructure code using popular security tools.
- **Customizable Reports**: Generate detailed reports in JSON or HTML format.
- **Dashboard for Issue Navigation**: Navigate and explore identified issues through an interactive dashboard. The dashboard categorizes and presents issues by severity, linter type, and more, providing an easy way to investigate and resolve problems.

- **Configurable Color Scheme**: Customize the color scheme for different severity levels (CRITICAL, HIGH, MEDIUM, LOW, INFO).
- **AI-Generated Insights**: Automatically infer severity and context for high-severity issues using OpenAI.
- **Caching for AI Responses**: To reduce repeated calls to OpenAI, Ai_sec caches AI-generated insights for faster subsequent runs.
- **Modular Linter Support**: Easily enable or disable linters through the configuration file.

## Installation

Ensure you are using Python 3.10 or above.

### Option 1: Using a Virtual Environment and Symbolic Links

1. **Ensure Python Version**

   - Verify you have Python 3.10 or later:
     ```bash
     python --version
     ```

2. **Create and Activate Virtual Environment**

   - **Create**:

     ```bash
     python -m venv myenv
     ```

   - **Activate**:
     - **Windows**:
       ```bash
       myenv\\Scripts\\activate
       ```
     - **macOS/Linux**:
       ```bash
       source myenv/bin/activate
       ```

3. **Install Ai_sec**
   ```bash
   pip install ai_sec
   ```

### Option 2: Installing Directly to System Python

1. **Ensure Python Version**

   - Verify you have Python 3.10 or later:
     ```bash
     python --version
     ```

2. **Install AI_Sec**
   ```bash
   python -m pip install ai_sec
   ```

### Setting Up

To configure AI_Sec, follow these steps:

1. You can export the default config by running `ai_sec export-config`.

2. The default configuration file will be exported to `~/.ai_sec/config.yaml`.

3. By default, Checkov is the main linter used, but you can enable TFLint and TFSec as needed if you have them installed.

4. Edit the `config.yaml` file to enable/disable linters and set the report output format.

## Sample Configuration

Here’s the default `config.yaml`
Before running AI_Sec, you need to set up the default configuration file. You can automatically export the default configuration to the `~/.ai_sec/config.yaml` directory by running the following command:

```bash
ai_sec export-config
```

```yaml
linters:
  tflint:
    enabled: false
  tfsec:
    enabled: false
  checkov:
    enabled: true
    framework: terraform # Default framework can also be Cloudformation
output:
  format: json
  save_to: ./reports/report.json
color_scheme:
  CRITICAL: "#FF6F61"
  HIGH: "#FFA07A"
  MEDIUM: "#FFD700"
  LOW: "#90EE90"
  INFO: "#B0C4DE"
```

## Open AI Insights

AI_Sec integrates with OpenAI to provide enhanced insights on infrastructure issues. This includes determining the severity of issues and providing additional context and resolution suggestions for critical and high-severity issues. These insights can be particularly useful in understanding the nature of the problems and how to resolve them.

### How to Enable OpenAI Insights

To enable OpenAI insights, you will need an API key from OpenAI

1. Set the OpenAI API Key: You must set an environment variable OPENAI_API_KEY with your OpenAI API key.
   You can export it in your terminal before running the tool:
   bash`   export OPENAI_API_KEY="your-openai-api-key"`
2. Enable OpenAI Insights in the Configuration: Ensure that the OpenAI integration is enabled in the configuration file. By default, if the API key is set, the insights will automatically be enabled when issues are found.

### How OpenAI Insights Work

When a linter detects an issue, AI_Sec sends a request to OpenAI to analyze the issue and provide:

**Severity**: The issue’s severity level (CRITICAL, HIGH, MEDIUM, or LOW).
**Context and Resolution**: For critical and high-severity issues, additional context and resolution suggestions will be provided.

These insights are added to the linting report and can be viewed in the AI_Sec Dashboard.

### Caching of OpenAI Responses

To avoid repeated API calls and improve performance, OpenAI responses are cached locally. The cache is created in the user’s home directory under ~/.ai_sec/openai_cache.json. This means if the same issue is analyzed multiple times, the tool will retrieve the result from the cache instead of querying OpenAI again.

Note: The cache key is generated based on the issue description and the framework used, so identical issues will have the same result retrieved from the cache.

### Important Considerations

**API Limits**: Depending on your OpenAI subscription, you may have limits on the number of requests. Using the cache can help minimize the number of API calls.
**Performance**: Querying OpenAI can add some additional time to the analysis, especially for large codebases or complex issues. The caching system helps mitigate this for repeated runs.
**Error Handling**: If an error occurs while querying OpenAI (e.g., invalid API key, connection issues), the tool will log the error and continue running without OpenAI insights.

## Commands

Here are some useful commands to interact with AI_Sec:

- `ai_sec run <path>`: Run the linters on the specified path and generate a report.
- `ai_sec export-config` - exports default config

### Cost Estimation

This tool uses the OpenAI API to derive insights. Below is an estimate of the cost per issue scanned:

- **Model**: gpt-4
- **Average tokens per issue**: ~300 tokens (200 input + 100 output)
- **Estimated cost per issue**: $0.012 (1.2 cents)
- **Example cost**:
  - 100 issues: ~$1.20
  - 1,000 issues: ~$12.00

If using **gpt-3.5-turbo**, the cost per issue is significantly lower:

- **Estimated cost per issue**: $0.0005 (0.05 cents)
- **Example cost**:
  - 100 issues: ~$0.05
  - 1,000 issues: ~$0.50

Costs may vary slightly depending on the length of the issue descriptions and the responses generated. For the latest pricing details, visit the [OpenAI pricing page](https://openai.com/pricing).

## Changelog

For detailed information about changes in each version, see the [Changelog](CHANGELOG.md).

## Contact

If you encounter any issues or have any suggestions, please feel free to send them to dev@darrenrabbitt.com. Thank you for your support!
