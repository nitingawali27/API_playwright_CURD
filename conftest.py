import pytest
import sys
import os
from datetime import datetime
from playwright.sync_api import sync_playwright

# ------------------------------
# Add project root to Python path
# ------------------------------
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

# ------------------------------
# Playwright fixture
# ------------------------------
@pytest.fixture(scope="session")
def playwright():
    """
    Fixture to start and stop Playwright for the test session.
    """
    with sync_playwright() as p:
        yield p

# ------------------------------
# Pytest HTML Report Configuration
# ------------------------------
def pytest_configure(config):
    """
    Configure pytest-html report path and name with datetime.
    """
    # Create Reports folder if it doesn't exist
    report_dir = r"D:\Playwright_Automation\Reports"
    os.makedirs(report_dir, exist_ok=True)

    # Generate report name with current date and time
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(report_dir, f"API_Test_Report_{now}.html")

    # Set pytest-html report path
    config.option.htmlpath = report_path
    config.option.self_contained_html = True  # Embed CSS/JS into report
