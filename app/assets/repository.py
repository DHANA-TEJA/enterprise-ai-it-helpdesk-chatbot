from app.database.db import get_db


class AssetRepository:

    @staticmethod
    def get_collection():
        return get_db()["assets"]

    @staticmethod
    def create(asset):
        return AssetRepository.get_collection().insert_one(asset)

    @staticmethod
    def get_all():
        return list(
            AssetRepository.get_collection().find()
        )

    @staticmethod
    def get_by_asset_id(asset_id):
        return AssetRepository.get_collection().find_one(
            {
                "asset_id": asset_id
            }
        )

    @staticmethod
    def update(asset_id, data):
        return AssetRepository.get_collection().update_one(
            {
                "asset_id": asset_id
            },
            {
                "$set": data
            }
        )

    @staticmethod
    def delete(asset_id):
        return AssetRepository.get_collection().delete_one(
            {
                "asset_id": asset_id
            }
        )