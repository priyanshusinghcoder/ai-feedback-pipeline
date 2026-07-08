from pydantic import BaseModel
from typing import List, Optional

class FeedbackTicket(BaseModel):
    id: int
    customer_name: str
    email: str
    message: str
    sentiment: Optional[str] = None
    tags: Optional[List[str]] = None
    ai_draft_response: Optional[str] = None

db_tickets = {}

KNOWLEDGE_BASE = [
    {"topic": "Billing", "content": "Our refund policy allows full refunds within 14 days of purchase. Contact billing@company.com."},
    {"topic": "Bug", "content": "Known issue with login token expiration. Clearing browser cache or updating to v2.1 fixes it."},
    {"topic": "Feature Request", "content": "Feature requests are logged in our public roadmap. Expected turnaround for evaluation is 5 business days."}
]
