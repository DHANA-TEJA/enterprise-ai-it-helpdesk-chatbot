from app.dashboard.repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_summary():

        return {

            "success": True,

            "dashboard": {

                "total_users":
                    DashboardRepository.total_users(),

                "total_tickets":
                    DashboardRepository.total_tickets(),

                "open_tickets":
                    DashboardRepository.open_tickets(),

                "resolved_tickets":
                    DashboardRepository.resolved_tickets(),

                "total_assets":
                    DashboardRepository.total_assets(),

                "total_conversations":
                    DashboardRepository.total_conversations()

            }

        }