from datetime import datetime

from app.tickets.repository import TicketRepository
from app.tickets.priority import PriorityDetector


class TicketService:

    @staticmethod
    def generate_ticket_id():
        count = len(TicketRepository.get_all()) + 1
        return f"INC-{1000 + count}"

    @staticmethod
    def create_ticket(data, user_id="Demo User"):

        priority, reason = PriorityDetector.detect(
            data["description"]
        )

        ticket = {
            "ticket_id": TicketService.generate_ticket_id(),
            "title": data["title"],
            "description": data["description"],
            "category": data.get("category", "General"),
            "priority": priority,
            "priority_reason": reason,
            "status": "Open",
            "created_by": user_id,
            "assigned_engineer": None,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }

        # Insert into MongoDB
        result = TicketRepository.create(ticket)

        # Convert ObjectId to string for JSON response
        ticket["_id"] = str(result.inserted_id)

        return {
            "success": True,
            "message": "Ticket created successfully.",
            "ticket": ticket
        }

    @staticmethod
    def get_all_tickets():

        tickets = TicketRepository.get_all()

        for ticket in tickets:
            ticket["_id"] = str(ticket["_id"])

        return tickets