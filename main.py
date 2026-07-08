from fastapi import FastAPI, HTTPException
from database import FeedbackTicket, db_tickets, KNOWLEDGE_BASE

app = FastAPI()

@app.post("/tickets/")
async def create_ticket(ticket: FeedbackTicket):
    db_tickets[ticket.id] = ticket
    return {"message": "Ticket received", "ticket_id": ticket.id}

@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: int):
    if ticket_id not in db_tickets:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_tickets[ticket_id]

@app.get("/knowledge-base/")
async def get_knowledge():
    return KNOWLEDGE_BASE
