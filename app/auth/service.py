import bcrypt
from datetime import datetime

from flask_jwt_extended import create_access_token

from app.auth.repository import UserRepository


class AuthService:

    ALLOWED_ROLES = [
        "Employee",
        "IT Support Engineer",
        "Administrator"
    ]

    @staticmethod
    def register_user(data):

        required_fields = [
            "full_name",
            "email",
            "password",
            "department",
            "role"
        ]

        # Check required fields
        for field in required_fields:

            if field not in data or not str(data[field]).strip():

                return {
                    "success": False,
                    "message": f"{field} is required."
                }

        email = data["email"].strip().lower()

        # Duplicate email
        existing_user = UserRepository.find_by_email(email)

        if existing_user:

            return {
                "success": False,
                "message": "Email already registered."
            }

        # Validate role
        role = data["role"]

        if role not in AuthService.ALLOWED_ROLES:

            return {
                "success": False,
                "message": "Invalid role."
            }

        # Hash Password
        hashed_password = bcrypt.hashpw(
            data["password"].encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        user = {

            "full_name": data["full_name"],

            "email": email,

            "password": hashed_password,

            "department": data["department"],

            "role": role,

            "is_active": True,

            "created_at": datetime.utcnow(),

            "updated_at": datetime.utcnow()
        }

        UserRepository.create_user(user)

        return {

            "success": True,

            "message": "User registered successfully."
        }

    @staticmethod
    def login_user(data):

        if "email" not in data or "password" not in data:

            return {

                "success": False,

                "message": "Email and password are required."
            }

        email = data["email"].lower()

        password = data["password"]

        user = UserRepository.find_by_email(email)

        if not user:

            return {

                "success": False,

                "message": "Invalid email or password."
            }

        valid_password = bcrypt.checkpw(

            password.encode("utf-8"),

            user["password"].encode("utf-8")

        )

        if not valid_password:

            return {

                "success": False,

                "message": "Invalid email or password."
            }

        access_token = create_access_token(

            identity=str(user["_id"]),

            additional_claims={

                "role": user["role"],

                "email": user["email"]

            }

        )

        return {

            "success": True,

            "message": "Login successful.",

            "access_token": access_token,

            "user": {

                "id": str(user["_id"]),

                "full_name": user["full_name"],

                "email": user["email"],

                "department": user["department"],

                "role": user["role"]

            }

        }

    @staticmethod
    def get_profile(user_id):

        user = UserRepository.find_by_id(user_id)

        if not user:

            return None

        return {

            "id": str(user["_id"]),

            "full_name": user["full_name"],

            "email": user["email"],

            "department": user["department"],

            "role": user["role"],

            "created_at": user["created_at"]

        }