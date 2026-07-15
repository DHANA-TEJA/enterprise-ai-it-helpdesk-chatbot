from bson import ObjectId
from app.database.db import get_db


class UserRepository:

    @staticmethod
    def get_collection():
        db = get_db()
        return db["users"]

    @staticmethod
    def create_user(user_data):
        """
        Create a new user
        """
        return UserRepository.get_collection().insert_one(user_data)

    @staticmethod
    def find_by_email(email):
        """
        Find user by email
        """
        return UserRepository.get_collection().find_one({
            "email": email
        })

    @staticmethod
    def find_by_id(user_id):
        """
        Find user by MongoDB ObjectId
        """
        return UserRepository.get_collection().find_one({
            "_id": ObjectId(user_id)
        })

    @staticmethod
    def get_all_users():
        """
        Get all users
        """
        return list(
            UserRepository.get_collection().find()
        )

    @staticmethod
    def update_user(user_id, update_data):
        """
        Update user details
        """
        return UserRepository.get_collection().update_one(
            {
                "_id": ObjectId(user_id)
            },
            {
                "$set": update_data
            }
        )

    @staticmethod
    def delete_user(user_id):
        """
        Delete user
        """
        return UserRepository.get_collection().delete_one(
            {
                "_id": ObjectId(user_id)
            }
        )