from flask import Blueprint, request, jsonify

from app.chatbot.service import ChatbotService

chatbot_bp = Blueprint(
    "chatbot",
    __name__,
    url_prefix="/chat"
)

service = ChatbotService()


@chatbot_bp.route("/", methods=["POST"])
def chat():
    """
    Enterprise AI Chatbot
    ---
    tags:
      - Chatbot

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true

        schema:
          type: object

          required:
            - message

          properties:

            message:
              type: string
              example: My laptop won't connect to Wi-Fi

    responses:

      200:
        description: AI Response
    """

    data = request.get_json()

    if not data or "message" not in data:

        return jsonify({
            "success": False,
            "message": "Message is required."
        }), 400

    result = service.chat(data["message"])

    return jsonify(result)