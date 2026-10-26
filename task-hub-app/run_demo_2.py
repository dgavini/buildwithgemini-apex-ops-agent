#!/usr/bin/env python3
"""
Live Visual Demo Scenario 2: High-Value Expense Review & Security Incident Mitigation.
Runs headed on DISPLAY=:1 in Chrome with visible typing & clicks,
capturing high-resolution screenshots.
"""
import os
import time
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = "/config/Desktop/BuildWithGemini/task-hub-app/demo_screenshots_scenario2"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

CHROME_PATH = "/usr/bin/google-chrome"
APP_URL = "http://localhost:5173"

def run_demo():
    print("=" * 65)
    print("🎬 STARTING LIVE DEMO SCENARIO 2 (SECURITY & HIGH-VALUE REVIEW)")
    print("=" * 65)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=False,
            slow_mo=600,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--start-maximized",
            ],
        )

        page = browser.new_page(viewport={"width": 1280, "height": 880})

        print(f"👉 Navigating to {APP_URL}...")
        page.goto(APP_URL)
        time.sleep(1.0)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "01_initial_state.png"))

        # ----------------------------------------------------
        # SCENARIO 2 - TASK 1: Security Architect Onboarding
        # ----------------------------------------------------
        print("\n👤 Task 1: Onboarding Security Lead (David Chen)...")
        page.click('[data-testid="tab-onboarding"]')
        time.sleep(0.5)

        page.fill('[data-testid="onboard-name"]', "David Chen")
        page.select_option('[data-testid="onboard-dept"]', "Security")
        page.fill('[data-testid="onboard-email"]', "d.chen@apex-sec.com")
        
        # Equip Laptop + ANC Headset
        page.check('[data-testid="onboard-equip-laptop"]')
        page.uncheck('[data-testid="onboard-equip-monitor"]')
        page.check('[data-testid="onboard-equip-headset"]')
        time.sleep(0.8)

        print("   -> Submitting Security Onboarding...")
        page.click('[data-testid="onboard-submit"]')
        page.wait_for_selector('[data-testid="onboard-success-card"]', timeout=5000)
        badge_text = page.inner_text(".badge-id")
        print(f"   ✅ Task 1 Complete! Issued Security Badge: {badge_text}")
        time.sleep(1.8)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "02_task1_security_badge.png"))

        # ----------------------------------------------------
        # SCENARIO 2 - TASK 2: High-Value Expense ($1,850 -> Manager Review)
        # ----------------------------------------------------
        print("\n💳 Task 2: Submitting High-Value Expense ($1,850.00)...")
        page.click('[data-testid="tab-expenses"]')
        time.sleep(0.8)

        page.select_option('[data-testid="expense-category"]', "Office Equipment")
        page.fill('[data-testid="expense-merchant"]', "Herman Miller Ergonomics")
        page.fill('[data-testid="expense-amount"]', "1850.00")
        page.select_option('[data-testid="expense-urgency"]', "Urgent")
        page.fill('[data-testid="expense-notes"]', "SOC Operations high-intensity ergonomic monitoring workstation")
        time.sleep(0.8)

        print("   -> Submitting claim and triggering policy check...")
        page.click('[data-testid="expense-submit"]')
        page.wait_for_selector('[data-testid="expense-success-card"]', timeout=5000)
        claim_id = page.inner_text(".receipt-card .font-mono")
        print(f"   ⚠️ Task 2 Complete! Claim {claim_id} flagged: 'Requires Manager Review' (>$500)")
        time.sleep(1.8)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "03_task2_manager_review_flag.png"))

        # ----------------------------------------------------
        # SCENARIO 2 - TASK 3: Database Replica Outage Triage
        # ----------------------------------------------------
        print("\n🚨 Task 3: Triaging Database Replication Latency...")
        page.click('[data-testid="tab-incidents"]')
        time.sleep(0.8)

        page.select_option('[data-testid="incident-severity"]', "P2 - High")
        page.select_option('[data-testid="incident-service"]', "PostgreSQL Cluster")
        page.fill('[data-testid="incident-title"]', "Read Replica Replication Lag Spike (>45s)")
        page.fill(
            '[data-testid="incident-resolution"]',
            "Recycled replica WAL buffers, boosted checkpoint completion target, and re-indexed session partition.",
        )
        page.select_option('[data-testid="incident-status"]', "Mitigated")
        time.sleep(0.8)

        print("   -> Recording incident mitigation...")
        page.click('[data-testid="incident-submit"]')
        page.wait_for_selector('[data-testid="incident-success-card"]', timeout=5000)
        inc_id = page.inner_text(".incident-card .font-mono")
        print(f"   ✅ Task 3 Complete! Incident Logged: {inc_id} (Status: Mitigated)")
        time.sleep(1.8)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "04_task3_mitigated_incident.png"))

        # Scroll to inspect Updated Activity Feed
        print("\n📋 Reviewing live updated audit feed...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2.0)
        page.screenshot(path=os.path.join(SCREENSHOT_DIR, "05_updated_audit_feed.png"))

        time.sleep(2.5)
        browser.close()

        print("\n" + "=" * 65)
        print("🎉 SCENARIO 2 DEMO COMPLETED SUCCESSFULLY!")
        print(f"📸 Screenshots captured in: {SCREENSHOT_DIR}")
        print("=" * 65)

if __name__ == "__main__":
    run_demo()
