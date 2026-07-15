from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager

from app.config import Config
from app.database.db import connect_db

# Authentication
from app.auth.routes import auth_bp

# Chatbot
from app.chatbot.routes import chatbot_bp

# Tickets
from app.tickets.routes import ticket_bp

# Conversations
from app.conversations.routes import conversation_bp

# Assets
from app.assets.routes import asset_bp

# Dashboard
from app.dashboard.routes import dashboard_bp

jwt = JWTManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.config["SWAGGER"] = {
        "title": "Enterprise AI IT Helpdesk API",
        "uiversion": 3,
        "version": "1.0.0",
        "description": "Enterprise AI IT Helpdesk Chatbot API Documentation",
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Bearer <JWT_TOKEN>"
            }
        }
    }

    Swagger(app)

    jwt.init_app(app)

    connect_db()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(conversation_bp)
    app.register_blueprint(asset_bp)
    app.register_blueprint(dashboard_bp)

    @app.route("/", methods=["GET"])
    def home():
        """
        Home API
        ---
        tags:
          - Home

        responses:
          200:
            description: API Running Successfully
        """

        return {
            "status": "success",
            "message": "Enterprise AI Helpdesk API is running",
            "database": "Connected"
        }, 200

    return app