from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.auth.service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


# -----------------------------
# Register
# -----------------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register User
    ---
    tags:
      - Authentication

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true

        schema:
          type: object
          required:
            - full_name
            - email
            - password
            - department
            - role

          properties:

            full_name:
              type: string
              example: Dhana Teja

            email:
              type: string
              example: dhana@gmail.com

            password:
              type: string
              example: Password@123

            department:
              type: string
              example: AI

            role:
              type: string
              example: Employee

    responses:

      201:
        description: User Registered

      400:
        description: Validation Error
    """

    data = request.get_json()

    result = AuthService.register_user(data)

    if result["success"]:
        return jsonify(result), 201

    return jsonify(result), 400


# -----------------------------
# Login
# -----------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Login User
    ---
    tags:
      - Authentication

    consumes:
      - application/json

    parameters:

      - in: body
        name: body
        required: true

        schema:
          type: object

          required:
            - email
            - password

          properties:

            email:
              type: string
              example: dhana@gmail.com

            password:
              type: string
              example: Password@123

    responses:

      200:
        description: Login Successful

      401:
        description: Invalid Credentials
    """

    data = request.get_json()

    result = AuthService.login_user(data)

    if result["success"]:
        return jsonify(result), 200

    return jsonify(result), 401


# -----------------------------
# Profile
# -----------------------------
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    """
    Logged In User Profile
    ---
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:

      200:
        description: User Profile

      401:
        description: Unauthorized
    """

    user_id = get_jwt_identity()

    profile = AuthService.get_profile(user_id)

    if not profile:

        return jsonify({

            "success": False,

            "message": "User not found."

        }), 404

    return jsonify({

        "success": True,

        "user": profile

    }), 200