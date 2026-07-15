from app.database.db import get_db


class DashboardRepository:

    @staticmethod
    def get_db():
        return get_db()

    @staticmethod
    def total_users():
        return DashboardRepository.get_db()["users"].count_documents({})

    @staticmethod
    def total_tickets():
        return DashboardRepository.get_db()["tickets"].count_documents({})

    @staticmethod
    def open_tickets():
        return DashboardRepository.get_db()["tickets"].count_documents(
            {
                "status": "Open"
            }
        )

    @staticmethod
    def resolved_tickets():
        return DashboardRepository.get_db()["tickets"].count_documents(
            {
                "status": "Resolved"
            }
        )

    @staticmethod
    def total_assets():
        return DashboardRepository.get_db()["assets"].count_documents({})

    @staticmethod
    def total_conversations():
        return DashboardRepository.get_db()["conversations"].count_documents({})