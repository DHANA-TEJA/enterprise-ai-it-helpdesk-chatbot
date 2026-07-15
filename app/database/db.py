from pymongo import MongoClient
from app.config import Config

client = None
db = None


def connect_db():
    global client, db

    try:
        client = MongoClient(Config.MONGO_URI)

        client.admin.command("ping")

        db = client["enterprise_ai_helpdesk"]

        print("=" * 60)
        print("✅ Connected to MongoDB Atlas")
        print(f"📂 Database : {db.name}")
        print("=" * 60)

        return db

    except Exception as e:
        print(e)
        raise e


def get_db():
    return db