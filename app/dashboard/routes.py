from flask import Blueprint, jsonify

from app.dashboard.service import DashboardService

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)


@dashboard_bp.route("/", methods=["GET"])
def dashboard_summary():
    """
    Dashboard Summary
    ---
    tags:
      - Dashboard
    responses:
      200:
        description: Dashboard statistics
    """

    return jsonify(DashboardService.get_summary()), 200