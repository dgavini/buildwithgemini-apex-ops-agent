#!/usr/bin/env python3
"""
Dedicated Live Demo: Task 3 - IT Incident & Support Triage.
Focuses specifically on infrastructure outage logging, severity routing,
mitigation note recording, and ticket generation on http://localhost:5173.
"""
import os
import time
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = "/config/Desktop/BuildWithGemini/task-hub-app/demo_task3_screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

CHROME_PATH = "/usr/bin/google-chrome"
APP_URL = "http://localhost:5173"

def run_task3_demo():
    print("=" * 65)
    print("🚨 STARTING DEDICATED LIVE DEMO: TASK 3 (IT INCIDENT TRIAGE)")
    print("=" * 65)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=False,
            slow_mo=800,  # Slow-mo for clear, deliberate presentation
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--start-maximized",
            ],
        )

        page = browser.new_page(viewport={"width": 1280, "height": 880})

        print(f"👉 Step 1: Navigating to {APP_URL}...")
        page.goto(APP_URL)
        time.sleep(1.0)

        # ----------------------------------------------------
        # 1. Switch directly to Task 3: Incident Triage
        # ----------------------------------------------------
        print("\n👉 Step 2: Clicking Tab '3. Incident Triage'...")
        page.click('[data-testid="tab-incidents"]')
        time.sleep(1.0)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "01_task3_empty_form.png"))

        # ----------------------------------------------------
        # 2. Fill Incident Parameters
        # ----------------------------------------------------
        severity = "P1 - Critical"
        service = "User Authentication"
        title = "JWT Token Verification Outage across Auth Cluster"
        resolution = "Flushed poisoned Redis session cache, deployed hotfix patch v2.14.1, and recycled all 16 Auth worker nodes."
        status = "Resolved"

        print(f"\n👉 Step 3: Selecting Severity [{severity}]...")
        page.select_option('[data-testid="incident-severity"]', severity)
        time.sleep(0.6)

        print(f"👉 Step 4: Selecting Affected Service [{service}]...")
        page.select_option('[data-testid="incident-service"]', service)
        time.sleep(0.6)

        print(f"👉 Step 5: Typing Incident Title: '{title}'...")
        page.fill('[data-testid="incident-title"]', title)
        time.sleep(0.8)

        print(f"👉 Step 6: Typing Resolution & Mitigation Steps: '{resolution}'...")
        page.fill('[data-testid="incident-resolution"]', resolution)
        time.sleep(0.8)

        print(f"👉 Step 7: Setting Current Status to [{status}]...")
        page.select_option('[data-testid="incident-status"]', status)
        time.sleep(0.8)

        # Capture form filled before clicking submit
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "02_task3_form_filled.png"))

        # ----------------------------------------------------
        # 3. Submit and Verify Outcome
        # ----------------------------------------------------
        print("\n👉 Step 8: Clicking 'Record Incident Resolution' button...")
        page.click('[data-testid="incident-submit"]')

        # Wait for success card
        page.wait_for_selector('[data-testid="incident-success-card"]', timeout=5000)
        inc_id = page.inner_text(".incident-card .font-mono")
        print(f"\n✅ SUCCESS: Incident ticket generated on screen: {inc_id}!")
        time.sleep(2.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "03_task3_ticket_card.png"))

        # ----------------------------------------------------
        # 4. View Live Activity Feed
        # ----------------------------------------------------
        print("\n👉 Step 9: Scrolling down to Live Activity Feed to verify audit stamp...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2.5)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "04_task3_activity_feed.png"))

        time.sleep(2.0)
        browser.close()

        print("\n" + "=" * 65)
        print(f"🎉 TASK 3 DEMO FINISHED! Ticket {inc_id} created and logged.")
        print(f"📸 Step-by-step screenshots saved to: {SCREENSHOT_DIR}")
        print("=" * 65)

if __name__ == "__main__":
    run_task3_demo()
