"""
Firestore Tools for Apex Operations Agent.
Provides read and write operations for the 'operations_tasks' collection.
"""
from datetime import datetime, timezone
from google.cloud import firestore

# IMPORTANT: Hardcode project ID as string.
# Do not read from google.auth.default() or GOOGLE_CLOUD_PROJECT
# to prevent project-number resolution issues on Agent Platform.
PROJECT_ID = "qwiklabs-gcp-04-6e08aeb7a54c"
COLLECTION_NAME = "operations_tasks"

_db = None

def get_db():
    global _db
    if _db is None:
        _db = firestore.Client(project=PROJECT_ID)
    return _db


def list_operations_tasks(task_type: str = "", status: str = "") -> list[dict]:
    """Lists operational tasks from Firestore with optional filtering.

    Args:
        task_type: Optional filter by task type ('Onboarding', 'Expense Claim', 'IT Incident').
        status: Optional filter by status ('Active', 'Approved', 'Pending', 'Resolved', 'Investigating').

    Returns:
        A list of task dictionaries.
    """
    db = get_db()
    query = db.collection(COLLECTION_NAME)

    if task_type:
        query = query.where("task_type", "==", task_type)
    if status:
        query = query.where("status", "==", status)

    docs = query.stream()
    results = []
    for doc in docs:
        data = doc.to_dict()
        results.append(data)
    return results


def get_operations_task(task_id: str) -> dict:
    """Retrieves a single operational task from Firestore by its task ID.

    Args:
        task_id: The ID of the task (e.g., 'EMP-4012', 'EXP-8841', 'INC-2090').

    Returns:
        The task document data or a not-found dictionary.
    """
    db = get_db()
    doc_ref = db.collection(COLLECTION_NAME).document(task_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return {"error": f"Task '{task_id}' not found in {COLLECTION_NAME}"}


def create_or_update_operations_task(
    task_id: str,
    task_type: str,
    title: str,
    details: str,
    status: str = "Active",
    priority: str = "Standard",
    assignee_or_requester: str = "General",
) -> dict:
    """Creates or updates an operational task in the Firestore backend.

    Args:
        task_id: Unique task identifier (e.g., 'EMP-5501', 'EXP-3320', 'INC-4401').
        task_type: The type of task ('Onboarding', 'Expense Claim', 'IT Incident').
        title: Short title summarizing the task.
        details: Specific details, equipment, receipt breakdown, or resolution steps.
        status: Status string ('Active', 'Approved', 'Pending', 'Resolved', 'Investigating').
        priority: Priority level ('Standard', 'High', 'Critical').
        assignee_or_requester: Responsible party or team.

    Returns:
        The recorded task dictionary with timestamp confirmation.
    """
    db = get_db()
    now_iso = datetime.now(timezone.utc).isoformat()
    doc_ref = db.collection(COLLECTION_NAME).document(task_id)

    existing = doc_ref.get()
    created_at = existing.to_dict().get("created_at", now_iso) if existing.exists else now_iso

    payload = {
        "task_id": task_id,
        "task_type": task_type,
        "title": title,
        "details": details,
        "status": status,
        "priority": priority,
        "assignee_or_requester": assignee_or_requester,
        "created_at": created_at,
        "updated_at": now_iso,
    }

    doc_ref.set(payload)
    return {"status": "SUCCESS", "task": payload}
