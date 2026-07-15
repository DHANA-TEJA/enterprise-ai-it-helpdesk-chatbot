from app.ai.gemini import GeminiClient
from app.chatbot.prompts import SYSTEM_PROMPT
from app.rag.retriever import KnowledgeRetriever

from app.tickets.service import TicketService
from app.conversations.service import ConversationService


class ChatbotService:

    def __init__(self):
        self.gemini = GeminiClient()
        self.retriever = KnowledgeRetriever()

    def needs_ticket(self, response):

        response = response.lower()

        keywords = [
            "ticket",
            "it support",
            "contact it",
            "contact the it team",
            "escalate",
            "unable to resolve",
            "cannot resolve",
            "support ticket"
        ]

        return any(keyword in response for keyword in keywords)

    def chat(self, message):

        print("=" * 60)
        print("CHAT REQUEST RECEIVED")
        print("=" * 60)

        knowledge = self.retriever.search(message)

        prompt = f"""
{SYSTEM_PROMPT}

You are an Enterprise AI IT Helpdesk Assistant.

Use ONLY the following company IT documentation.

Knowledge Base:

{knowledge}

Employee Question:

{message}

Instructions:

1. Use ONLY the provided knowledge base.
2. If more information is required, ask follow-up questions.
3. If the issue cannot be resolved, recommend creating an IT support ticket.
4. Do not invent troubleshooting steps.

Answer:
"""

        response = self.gemini.generate_response(prompt)

        result = {
            "success": True,
            "knowledge_used": knowledge,
            "response": response
        }

        ticket_created = False
        ticket_id = None

        if self.needs_ticket(response):

            print("Ticket Required")

            ticket = TicketService.create_ticket(
                {
                    "title": message,
                    "description": message,
                    "category": "General"
                }
            )

            result["ticket"] = ticket["ticket"]

            ticket_created = True
            ticket_id = ticket["ticket"]["ticket_id"]

        print("Saving Conversation...")

        ConversationService.save_conversation(
            user_id="Demo User",
            question=message,
            response=response,
            ticket_created=ticket_created,
            ticket_id=ticket_id
        )

        print("Conversation Saved Successfully")

        print("=" * 60)

        return result