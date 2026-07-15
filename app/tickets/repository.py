from bson import ObjectId

from app.database.db import get_db


class TicketRepository:

    @staticmethod
    def get_collection():
        return get_db()["tickets"]

    @staticmethod
    def create(ticket):
        return TicketRepository.get_collection().insert_one(ticket)

    @staticmethod
    def get_all():
        return list(
            TicketRepository.get_collection().find()
        )

    @staticmethod
    def get_by_ticket_id(ticket_id):

        return TicketRepository.get_collection().find_one(
            {
                "ticket_id": ticket_id
            }
        )

    @staticmethod
    def update(ticket_id, data):

        return TicketRepository.get_collection().update_one(
            {
                "ticket_id": ticket_id
            },
            {
                "$set": data
            }
        )

    @staticmethod
    def delete(ticket_id):

        return TicketRepository.get_collection().delete_one(
            {
                "ticket_id": ticket_id
            }
        )