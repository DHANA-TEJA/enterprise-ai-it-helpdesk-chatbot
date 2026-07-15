from flask import Blueprint, jsonify

from app.conversations.service import ConversationService

conversation_bp = Blueprint(
    "conversations",
    __name__,
    url_prefix="/conversations"
)


@conversation_bp.route("/", methods=["GET"])
def get_conversations():
    """
    Get Conversation History
    ---
    tags:
      - Conversations

    responses:
      200:
        description: Conversation History
    """

    conversations = ConversationService.get_all_conversations()

    return jsonify({
        "success": True,
        "count": len(conversations),
        "conversations": conversations
    }), 200