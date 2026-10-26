# Apex Operations Hub — Task Completion Guide

This guide provides step-by-step instructions for completing each of the three distinct tasks on **Apex Operations Hub** (`http://localhost:5173`), covering both **manual UI steps** and **automated AI agent execution (Playwright / DOM selectors)**.

---

## Quick Navigation

- [Application URL](#application-url)
- [Task 1: Employee Onboarding](#task-1-employee-onboarding)
- [Task 2: Expense Claim Submission](#task-2-expense-claim-submission)
- [Task 3: IT Incident & Support Triage](#task-3-it-incident--support-triage)
- [Live Activity Audit Verification](#live-activity-audit-verification)
- [Sample Playwright Automation Code](#sample-playwright-automation-code)

---

## Application URL

- **URL:** `http://localhost:5173`
- **Application Title:** Apex Operations Hub

---

## Task 1: Employee Onboarding

### Purpose
Provision new hire identity, select department access tier, assign physical hardware, and generate an employee badge (`EMP-XXXX`).

### Step-by-Step UI Execution
1. Click the **"1. Employee Onboarding"** tab at the top (`data-testid="tab-onboarding"`).
2. Enter the new employee's **Full Name** in the `Full Name *` input field.
3. Select the employee's **Department** from the dropdown:
   - `Engineering`, `Product`, `Marketing`, `Sales`, or `Security`.
4. Enter their corporate **Work Email** in the email input field.
5. In **Hardware Equipment Needed**, check the appropriate gear:
   - `Laptop (16" Pro)`
   - `4K External Monitor`
   - `ANC Headset`
6. Select or verify the **Start Date**.
7. Click the blue **"Submit Employee Onboarding"** button.

### Success Verification
- A blue confirmation banner displays: `"Onboarding Completed Successfully"`.
- An employee badge appears showing the generated **Employee ID** (`EMP-XXXX`), assigned department, and allocated equipment.
- A new entry is appended to the **Live Activity & Task Audit Log** at the bottom.

### DOM Selectors for Automation
| Element | Selector / Test ID | Example Value |
|---|---|---|
| Tab Switcher | `[data-testid="tab-onboarding"]` | Click |
| Full Name | `[data-testid="onboard-name"]` | `"Sarah Jenkins"` |
| Department | `[data-testid="onboard-dept"]` | `"Engineering"` |
| Work Email | `[data-testid="onboard-email"]` | `"s.jenkins@company.com"` |
| Laptop Checkbox | `[data-testid="onboard-equip-laptop"]` | `true` |
| Monitor Checkbox | `[data-testid="onboard-equip-monitor"]` | `true` |
| Headset Checkbox | `[data-testid="onboard-equip-headset"]` | `false` |
| Start Date | `[data-testid="onboard-date"]` | `"2026-11-01"` |
| Submit Button | `[data-testid="onboard-submit"]` | Click |
| Success Confirmation | `[data-testid="onboard-success-card"]` | Wait for visible |

---

## Task 2: Expense Claim Submission

### Purpose
Submit vendor receipts and business expenses, triggering automatic policy checks ($\le \$500$ auto-approves, $> \$500$ routes to manager review).

### Step-by-Step UI Execution
1. Click the **"2. Expense Claims"** tab at the top (`data-testid="tab-expenses"`).
2. Select the **Expense Category**:
   - `Software & Tools`, `Travel & Lodging`, `Client Meals`, or `Office Equipment`.
3. Enter the **Merchant / Vendor Name** (e.g., `AWS Cloud Services` or `Delta Airlines`).
4. Enter the **Amount (USD)** (e.g., `120.50` or `1250.00`).
5. Select the **Urgency**:
   - `Standard` (Regular Payroll reimbursement).
   - `Urgent` (Express 24h Reimbursement).
6. Enter an optional **Business Justification / Purpose**.
7. Click the green **"Submit Expense Claim"** button.

### Success Verification
- **If Amount $\le \$500$**: An emerald badge appears with status: `"Claim Filed: Auto-Approved"`.
- **If Amount $> \$500$**: An amber warning badge appears: `"Claim Filed: Requires Manager Review"`.
- A receipt card is issued displaying the generated **Claim ID** (`EXP-XXXX`), total amount, and vendor.
- The claim is recorded in the **Live Activity Log**.

### DOM Selectors for Automation
| Element | Selector / Test ID | Example Value |
|---|---|---|
| Tab Switcher | `[data-testid="tab-expenses"]` | Click |
| Category Dropdown | `[data-testid="expense-category"]` | `"Software & Tools"` |
| Merchant Name | `[data-testid="expense-merchant"]` | `"Datadog Monitoring"` |
| Amount (USD) | `[data-testid="expense-amount"]` | `350.00` |
| Urgency Dropdown | `[data-testid="expense-urgency"]` | `"Standard"` |
| Purpose / Notes | `[data-testid="expense-notes"]` | `"Production APM licenses"` |
| Submit Button | `[data-testid="expense-submit"]` | Click |
| Success Confirmation | `[data-testid="expense-success-card"]` | Wait for visible |

---

## Task 3: IT Incident & Support Triage

### Purpose
Record, triage, and log resolution actions for infrastructure outages and service degradations.

### Step-by-Step UI Execution
1. Click the **"3. Incident Triage"** tab at the top (`data-testid="tab-incidents"`).
2. Select the **Severity Level**:
   - `P1 - Critical (Outage / Revenue Impact)`
   - `P2 - High (Degraded Performance)`
   - `P3 - Normal (Minor Bug / Non-blocking)`
3. Select the **Affected Service**:
   - `Payment Gateway`, `User Authentication`, `PostgreSQL Cluster`, `Cloud CDN`, or `Order Processing`.
4. Enter the **Incident Title** summarizing the event.
5. In **Action / Resolution Taken**, enter technical mitigation notes describing what was done to fix or stabilize the service.
6. Select the **Current Status**:
   - `Resolved (Fully Operational)`
   - `Mitigated (Workaround In Place)`
   - `Investigating (Monitoring)`
7. Click the rose **"Record Incident Resolution"** button.

### Success Verification
- A confirmation card appears displaying the **Incident ID** (`INC-XXXX`), colored severity pill, service name, and timestamp.
- The incident resolution is permanently stamped in the **Live Activity Log**.

### DOM Selectors for Automation
| Element | Selector / Test ID | Example Value |
|---|---|---|
| Tab Switcher | `[data-testid="tab-incidents"]` | Click |
| Severity Dropdown | `[data-testid="incident-severity"]` | `"P1 - Critical"` |
| Affected Service | `[data-testid="incident-service"]` | `"Payment Gateway"` |
| Incident Title | `[data-testid="incident-title"]` | `"Stripe Webhook Timeout Spike"` |
| Resolution Notes | `[data-testid="incident-resolution"]` | `"Scaled worker pods from 4 to 12"` |
| Status Dropdown | `[data-testid="incident-status"]` | `"Resolved"` |
| Submit Button | `[data-testid="incident-submit"]` | Click |
| Success Confirmation | `[data-testid="incident-success-card"]` | Wait for visible |

---

## Live Activity Audit Verification

After completing any task, verify that the entry appears in the activity feed:
- **Feed Container:** `[data-testid="activity-feed"]`
- **Activity Item:** `[data-testid="activity-item"]`
- Filter buttons allow filtering between **All**, **Onboarding**, **Expenses**, and **Incidents**.

---

## Sample Playwright Automation Code

The following complete Python snippet demonstrates how an AI agent uses Playwright to complete each of the three tasks:

```python
import asyncio
from playwright.async_api import async_playwright

async def complete_onboarding_task(page, name: str, dept: str, email: str):
    await page.click('[data-testid="tab-onboarding"]')
    await page.fill('[data-testid="onboard-name"]', name)
    await page.select_option('[data-testid="onboard-dept"]', dept)
    await page.fill('[data-testid="onboard-email"]', email)
    await page.check('[data-testid="onboard-equip-laptop"]')
    await page.check('[data-testid="onboard-equip-monitor"]')
    await page.click('[data-testid="onboard-submit"]')
    await page.wait_for_selector('[data-testid="onboard-success-card"]')
    print(f"Task 1 Complete: Onboarded {name}")

async def complete_expense_task(page, merchant: str, amount: float, category: str):
    await page.click('[data-testid="tab-expenses"]')
    await page.select_option('[data-testid="expense-category"]', category)
    await page.fill('[data-testid="expense-merchant"]', merchant)
    await page.fill('[data-testid="expense-amount"]', str(amount))
    await page.click('[data-testid="expense-submit"]')
    await page.wait_for_selector('[data-testid="expense-success-card"]')
    print(f"Task 2 Complete: Expense for ${amount} at {merchant}")

async def complete_incident_task(page, severity: str, service: str, title: str, resolution: str):
    await page.click('[data-testid="tab-incidents"]')
    await page.select_option('[data-testid="incident-severity"]', severity)
    await page.select_option('[data-testid="incident-service"]', service)
    await page.fill('[data-testid="incident-title"]', title)
    await page.fill('[data-testid="incident-resolution"]', resolution)
    await page.click('[data-testid="incident-submit"]')
    await page.wait_for_selector('[data-testid="incident-success-card"]')
    print(f"Task 3 Complete: Incident logged - {title}")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://localhost:5173")

        # Execute Task 1
        await complete_onboarding_task(page, "Elena Rostova", "Engineering", "e.rostova@company.com")
        
        # Execute Task 2
        await complete_expense_task(page, "GitHub Enterprise", 420.00, "Software & Tools")

        # Execute Task 3
        await complete_incident_task(
            page, 
            severity="P1 - Critical", 
            service="Payment Gateway", 
            title="Gateway TLS Handshake Errors", 
            resolution="Rotated expired intermediate SSL certificate"
        )

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```
