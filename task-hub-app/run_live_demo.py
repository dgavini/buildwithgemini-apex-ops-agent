#!/usr/bin/env python3
"""
Live Visual Demo: Apex Operations Agent completing all 3 tasks in the React UI.
Runs headed on DISPLAY=:1 so the user watches every step live in Chrome,
and captures high-resolution screenshots of each completed task step.
"""
import os
import time
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = "/config/Desktop/BuildWithGemini/task-hub-app/demo_screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

CHROME_PATH = "/usr/bin/google-chrome"
APP_URL = "http://localhost:5173"

def run_demo():
    print("=" * 60)
    print("🎬 STARTING LIVE AGENT UI DEMO ON YOUR SCREEN")
    print("=" * 60)

    with sync_playwright() as p:
        # Launch Chrome on the desktop screen (DISPLAY=:1)
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=False,
            slow_mo=500,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--start-maximized",
            ],
        )

        page = browser.new_page(viewport={"width": 1280, "height": 850})

        print(f"👉 Step 1: Navigating to {APP_URL}...")
        page.goto(APP_URL)
        time.sleep(1.0)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "01_initial_dashboard.png"))

        # ----------------------------------------------------
        # TASK 1: Employee Onboarding
        # ----------------------------------------------------
        print("\n👤 Executing Task 1: Employee Onboarding...")
        page.click('[data-testid="tab-onboarding"]')
        time.sleep(0.5)

        page.fill('[data-testid="onboard-name"]', "Jessica Alba")
        page.select_option('[data-testid="onboard-dept"]', "Engineering")
        page.fill('[data-testid="onboard-email"]', "j.alba@company.com")
        page.check('[data-testid="onboard-equip-laptop"]')
        page.check('[data-testid="onboard-equip-monitor"]')
        time.sleep(0.8)

        print("   -> Submitting onboarding form...")
        page.click('[data-testid="onboard-submit"]')
        page.wait_for_selector('[data-testid="onboard-success-card"]', timeout=5000)
        badge_text = page.inner_text(".badge-id")
        print(f"   ✅ Task 1 Completed! Generated Badge: {badge_text}")
        time.sleep(1.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "02_task1_onboard_success.png"))

        # ----------------------------------------------------
        # TASK 2: Expense Claim
        # ----------------------------------------------------
        print("\n💳 Executing Task 2: Expense Claim Submission...")
        page.click('[data-testid="tab-expenses"]')
        time.sleep(0.8)

        page.select_option('[data-testid="expense-category"]', "Software & Tools")
        page.fill('[data-testid="expense-merchant"]', "OpenAI & Anthropic API Credits")
        page.fill('[data-testid="expense-amount"]', "420.00")
        page.select_option('[data-testid="expense-urgency"]', "Urgent")
        page.fill('[data-testid="expense-notes"]', "Monthly LLM API quota billing for core product")
        time.sleep(0.8)

        print("   -> Submitting expense claim...")
        page.click('[data-testid="expense-submit"]')
        page.wait_for_selector('[data-testid="expense-success-card"]', timeout=5000)
        claim_id = page.inner_text(".receipt-card .font-mono")
        print(f"   ✅ Task 2 Completed! Filed Receipt: {claim_id} (Auto-Approved under $500)")
        time.sleep(1.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "03_task2_expense_success.png"))

        # ----------------------------------------------------
        # TASK 3: IT Incident & Support Triage
        # ----------------------------------------------------
        print("\n🚨 Executing Task 3: IT Incident Triage...")
        page.click('[data-testid="tab-incidents"]')
        time.sleep(0.8)

        page.select_option('[data-testid="incident-severity"]', "P1 - Critical")
        page.select_option('[data-testid="incident-service"]', "Payment Gateway")
        page.fill('[data-testid="incident-title"]', "Cloudflare DNS Resolution Degradation")
        page.fill(
            '[data-testid="incident-resolution"]',
            "Traffic rerouted to secondary multi-region provider; zero transaction drops recorded.",
        )
        page.select_option('[data-testid="incident-status"]', "Resolved")
        time.sleep(0.8)

        print("   -> Recording incident resolution...")
        page.click('[data-testid="incident-submit"]')
        page.wait_for_selector('[data-testid="incident-success-card"]', timeout=5000)
        inc_id = page.inner_text(".incident-card .font-mono")
        print(f"   ✅ Task 3 Completed! Resolved Ticket: {inc_id}")
        time.sleep(1.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "04_task3_incident_success.png"))

        # Scroll to inspect Live Activity Log
        print("\n📋 Showing Live Activity Log at bottom...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "05_activity_feed_summary.png"))

        time.sleep(2.0)
        browser.close()

        print("\n" + "=" * 60)
        print("🎉 ALL 3 TASKS COMPLETED IN THE UI BY THE AGENT!")
        print(f"📸 Screenshots saved to: {SCREENSHOT_DIR}")
        print("=" * 60)

if __name__ == "__main__":
    run_demo()
