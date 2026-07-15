from app.database.db import get_db


class ConversationRepository:

    @staticmethod
    def get_collection():
        return get_db()["conversations"]

    @staticmethod
    def save(conversation):
        return ConversationRepository.get_collection().insert_one(conversation)

    @staticmethod
    def get_all():
        return list(
            ConversationRepository.get_collection().find()
        )