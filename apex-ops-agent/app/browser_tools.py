"""
Playwright Browser Automation Tools for Apex Operations Hub React Application.
Allows the agent to interact directly with the web UI at http://localhost:5173.
"""
from playwright.sync_api import sync_playwright

APP_URL = "http://localhost:5173"
CHROME_PATH = "/usr/bin/google-chrome"


def automate_ui_employee_onboarding(
    full_name: str,
    department: str = "Engineering",
    work_email: str = "",
    equip_laptop: bool = True,
    equip_monitor: bool = False,
    equip_headset: bool = False,
) -> dict:
    """Automates employee onboarding by driving the React web UI in the browser.

    Args:
        full_name: The full name of the employee (e.g., 'Sarah Jenkins').
        department: Department choice ('Engineering', 'Product', 'Marketing', 'Sales', 'Security').
        work_email: Work email address (e.g., 's.jenkins@company.com').
        equip_laptop: Whether to provision a 16\" Pro Laptop.
        equip_monitor: Whether to provision a 4K External Monitor.
        equip_headset: Whether to provision an ANC Headset.

    Returns:
        A dictionary with the submission status, generated Employee ID, and details.
    """
    if not work_email:
        clean_name = full_name.lower().replace(" ", ".")
        work_email = f"{clean_name}@company.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"],
        )
        page = browser.new_page()
        page.goto(APP_URL)

        # 1. Switch to Onboarding tab
        page.click('[data-testid="tab-onboarding"]')

        # 2. Fill form inputs
        page.fill('[data-testid="onboard-name"]', full_name)
        page.select_option('[data-testid="onboard-dept"]', department)
        page.fill('[data-testid="onboard-email"]', work_email)

        if equip_laptop:
            page.check('[data-testid="onboard-equip-laptop"]')
        else:
            page.uncheck('[data-testid="onboard-equip-laptop"]')

        if equip_monitor:
            page.check('[data-testid="onboard-equip-monitor"]')
        else:
            page.uncheck('[data-testid="onboard-equip-monitor"]')

        if equip_headset:
            page.check('[data-testid="onboard-equip-headset"]')
        else:
            page.uncheck('[data-testid="onboard-equip-headset"]')

        # 3. Submit
        page.click('[data-testid="onboard-submit"]')

        # 4. Wait for confirmation card
        page.wait_for_selector('[data-testid="onboard-success-card"]', timeout=5000)
        badge_id = page.inner_text(".badge-id")

        browser.close()

        return {
            "status": "SUCCESS",
            "task_type": "Employee Onboarding",
            "employee_id": badge_id,
            "full_name": full_name,
            "department": department,
            "email": work_email,
            "message": f"Successfully completed onboarding on the web UI for {full_name} ({badge_id}).",
        }


def automate_ui_expense_claim(
    merchant: str,
    amount: float,
    category: str = "Software & Tools",
    urgency: str = "Standard",
    notes: str = "",
) -> dict:
    """Automates filing an expense claim by driving the React web UI in the browser.

    Args:
        merchant: Name of the merchant or vendor (e.g., 'AWS Cloud Services', 'JetBrains').
        amount: Dollar amount (e.g., 149.50).
        category: Category ('Software & Tools', 'Travel & Lodging', 'Client Meals', 'Office Equipment').
        urgency: Urgency choice ('Standard', 'Urgent').
        notes: Optional business justification notes.

    Returns:
        A dictionary with the submission status, generated Claim ID, and approval routing.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"],
        )
        page = browser.new_page()
        page.goto(APP_URL)

        # 1. Switch to Expenses tab
        page.click('[data-testid="tab-expenses"]')

        # 2. Fill form inputs
        page.select_option('[data-testid="expense-category"]', category)
        page.fill('[data-testid="expense-merchant"]', merchant)
        page.fill('[data-testid="expense-amount"]', str(amount))
        page.select_option('[data-testid="expense-urgency"]', urgency)
        if notes:
            page.fill('[data-testid="expense-notes"]', notes)

        # 3. Submit
        page.click('[data-testid="expense-submit"]')

        # 4. Wait for confirmation card
        page.wait_for_selector('[data-testid="expense-success-card"]', timeout=5000)
        claim_id = page.inner_text(".receipt-card .font-mono")
        policy_status = "Auto-Approved" if amount <= 500 else "Requires Manager Review"

        browser.close()

        return {
            "status": "SUCCESS",
            "task_type": "Expense Claim",
            "claim_id": claim_id,
            "merchant": merchant,
            "amount": amount,
            "approval_status": policy_status,
            "message": f"Successfully filed expense claim on web UI: {claim_id} for ${amount:.2f} at {merchant} ({policy_status}).",
        }


def automate_ui_incident_triage(
    severity: str,
    service: str,
    title: str,
    resolution: str,
    status: str = "Resolved",
) -> dict:
    """Automates logging and resolving an IT incident by driving the React web UI.

    Args:
        severity: Severity level ('P1 - Critical', 'P2 - High', 'P3 - Normal').
        service: Affected service ('Payment Gateway', 'User Authentication', 'PostgreSQL Cluster', 'Cloud CDN', 'Order Processing').
        title: Short title summarizing the incident.
        resolution: Action taken or mitigation applied.
        status: Current status ('Resolved', 'Mitigated', 'Investigating').

    Returns:
        A dictionary with the submission status, generated Incident ID, and resolution summary.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"],
        )
        page = browser.new_page()
        page.goto(APP_URL)

        # 1. Switch to Incidents tab
        page.click('[data-testid="tab-incidents"]')

        # 2. Fill form inputs
        page.select_option('[data-testid="incident-severity"]', severity)
        page.select_option('[data-testid="incident-service"]', service)
        page.fill('[data-testid="incident-title"]', title)
        page.fill('[data-testid="incident-resolution"]', resolution)
        page.select_option('[data-testid="incident-status"]', status)

        # 3. Submit
        page.click('[data-testid="incident-submit"]')

        # 4. Wait for confirmation card
        page.wait_for_selector('[data-testid="incident-success-card"]', timeout=5000)
        inc_id = page.inner_text(".incident-card .font-mono")

        browser.close()

        return {
            "status": "SUCCESS",
            "task_type": "IT Incident",
            "incident_id": inc_id,
            "title": title,
            "service": service,
            "severity": severity,
            "status_applied": status,
            "message": f"Successfully recorded incident resolution on web UI: {inc_id} ({severity}) - {title}.",
        }
