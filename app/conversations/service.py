from datetime import datetime

from app.conversations.repository import ConversationRepository


class ConversationService:

    @staticmethod
    def save_conversation(
        user_id,
        question,
        response,
        ticket_created=False,
        ticket_id=None
    ):

        print("Inside Conversation Service")

        conversation = {

            "user_id": user_id,

            "question": question,

            "response": response,

            "ticket_created": ticket_created,

            "ticket_id": ticket_id,

            "created_at": datetime.utcnow().isoformat()

        }

        print("Conversation Data:")
        print(conversation)

        result = ConversationRepository.save(conversation)

        print("MongoDB Inserted ID:", result.inserted_id)

        conversation["_id"] = str(result.inserted_id)

        return conversation

    @staticmethod
    def get_all_conversations():

        conversations = ConversationRepository.get_all()

        for conversation in conversations:
            conversation["_id"] = str(conversation["_id"])

        return conversations