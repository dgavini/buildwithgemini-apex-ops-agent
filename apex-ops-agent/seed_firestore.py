"""
Firestore Seed Script for Apex Operations Hub.
Seeds the 'operations_tasks' collection with initial task items.
"""
from datetime import datetime, timezone
from google.cloud import firestore

# IMPORTANT: Hardcode project ID as string.
# Do not read from google.auth.default() or GOOGLE_CLOUD_PROJECT
# to prevent project-number resolution issues on Agent Platform.
PROJECT_ID = "qwiklabs-gcp-04-6e08aeb7a54c"
COLLECTION_NAME = "operations_tasks"

SEED_ITEMS = [
    {
        "task_id": "EMP-4012",
        "task_type": "Onboarding",
        "title": "Onboard Alex Rivera",
        "status": "Active",
        "priority": "Standard",
        "details": "Product & Design • a.rivera@company.com • Equipment: MacBook Pro 16\", 4K UltraFine Monitor",
        "assignee_or_requester": "HR Operations",
        "created_at": "2026-10-26T10:14:00Z",
        "updated_at": "2026-10-26T10:14:00Z",
    },
    {
        "task_id": "EXP-8841",
        "task_type": "Expense Claim",
        "title": "$149.00 - JetBrains All Products Pack",
        "status": "Approved",
        "priority": "Standard",
        "details": "Software & Tools • Auto-Approved • Standard priority • JetBrains",
        "assignee_or_requester": "Engineering Team",
        "created_at": "2026-10-26T11:02:00Z",
        "updated_at": "2026-10-26T11:02:00Z",
    },
    {
        "task_id": "INC-2090",
        "task_type": "IT Incident",
        "title": "P1 - Critical: Payment Gateway 502 Spike",
        "status": "Resolved",
        "priority": "Critical",
        "details": "Payment Gateway • Mitigated • Scaled worker pods from 4 to 12 and purged Redis connection pool",
        "assignee_or_requester": "SRE On-Call",
        "created_at": "2026-10-26T12:30:00Z",
        "updated_at": "2026-10-26T12:45:00Z",
    },
    {
        "task_id": "EMP-7719",
        "task_type": "Onboarding",
        "title": "Onboard Marcus Vance",
        "status": "Active",
        "priority": "Standard",
        "details": "Security & IT • m.vance@company.com • Equipment: Laptop 16\" Pro, ANC Headset",
        "assignee_or_requester": "HR Operations",
        "created_at": "2026-10-26T14:10:00Z",
        "updated_at": "2026-10-26T14:10:00Z",
    },
]

def seed_firestore():
    print(f"Connecting to Firestore for project: {PROJECT_ID}...")
    db = firestore.Client(project=PROJECT_ID)
    collection = db.collection(COLLECTION_NAME)

    for item in SEED_ITEMS:
        doc_ref = collection.document(item["task_id"])
        doc_ref.set(item)
        print(f"Seeded task: {item['task_id']} - {item['title']} ({item['task_type']})")

    print(f"\nSuccessfully seeded {len(SEED_ITEMS)} tasks into '{COLLECTION_NAME}' collection.")

if __name__ == "__main__":
    seed_firestore()
