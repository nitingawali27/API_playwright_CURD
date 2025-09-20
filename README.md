# Playwright API Automation Project

## Project Overview
This project is designed to automate API testing using **Python**, **Playwright**, and **pytest**.  
It supports **GET**, **POST**, **PUT**, and **DELETE** requests, with **common verification functions** and **logging**.

---

## Project Structure

Playwright_Automation/
│
├── Utilities/
│ ├── api_client.py # Handles GET, POST, PUT, DELETE requests
│ ├── api_url.py # Stores all API endpoints
│ ├── payload.py # Stores payloads for POST and PUT requests
│ ├── common_verifications.py # Common assertion functions
│ └── logger.py # Logger configuration
│
├── Tests/
│ ├── test_CURD.py # CRUD API tests
│ └── test_GET.py # GET API tests
│
├── Reports/ # HTML test reports (generated)
├── Logs/ # Log files (generated)
├── requirements.txt # Python dependencies
└── README.md

---

## Prerequisites

- Python 3.12+
- Virtual environment (`venv`)
- Installed packages:

```bash
pip install -r requirements.txt
Playwright browsers installed:


playwright install
Running Tests
Run all tests with verbose output:


pytest -v
Generate HTML report:


pytest --html=Reports/API_Test_Report.html
Features
API Client for GET, POST, PUT, DELETE requests

Common verifications: status code, headers, JSON key validation, JSON schema

Payloads and URLs stored separately for maintainability

Automatic logging of requests and responses

HTML reports with timestamped filenames

Logging
Logs are saved in Logs/ folder with date-time format:
API_Test_Log_YYYY-MM-DD_HH-MM-SS.log

Console output also includes logging information.

Notes
Ensure your virtual environment is activated before running tests

API key and headers are stored in Utilities/api_client.py for reuse

Modify payload.py for different POST/PUT test data

Author
Nitin Gawali
Senior QA Engineer

