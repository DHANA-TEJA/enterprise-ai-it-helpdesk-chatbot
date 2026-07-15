from flask import Blueprint, request, jsonify

from app.tickets.service import TicketService

ticket_bp = Blueprint(
    "tickets",
    __name__,
    url_prefix="/tickets"
)


@ticket_bp.route("/", methods=["POST"])
def create_ticket():
    """
    Create Support Ticket
    ---
    tags:
      - Tickets

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object

          required:
            - title
            - description

          properties:
            title:
              type: string
              example: Laptop Wi-Fi Issue

            description:
              type: string
              example: Laptop cannot connect to office Wi-Fi.

            category:
              type: string
              example: Network

    responses:
      201:
        description: Ticket Created
    """

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required."
        }), 400

    if "title" not in data or "description" not in data:
        return jsonify({
            "success": False,
            "message": "Title and Description are required."
        }), 400

    result = TicketService.create_ticket(data)

    return jsonify(result), 201


@ticket_bp.route("/", methods=["GET"])
def get_all_tickets():
    """
    Get All Tickets
    ---
    tags:
      - Tickets

    responses:
      200:
        description: List of Tickets
    """

    tickets = TicketService.get_all_tickets()

    return jsonify({
        "success": True,
        "count": len(tickets),
        "tickets": tickets
    }), 200