from app.assets.repository import AssetRepository


class AssetService:

    @staticmethod
    def generate_asset_id():

        count = len(
            AssetRepository.get_all()
        ) + 1

        return f"AST-{1000 + count}"

    @staticmethod
    def create_asset(data):

        asset = {

            "asset_id": AssetService.generate_asset_id(),

            "device_name": data["device_name"],

            "asset_type": data["asset_type"],

            "manufacturer": data["manufacturer"],

            "serial_number": data["serial_number"],

            "assigned_to": data["assigned_to"],

            "department": data["department"],

            "status": data.get(
                "status",
                "Active"
            )

        }

        result = AssetRepository.create(asset)

        asset["_id"] = str(
            result.inserted_id
        )

        return {
            "success": True,
            "message": "Asset added successfully.",
            "asset": asset
        }

    @staticmethod
    def get_all_assets():

        assets = AssetRepository.get_all()

        for asset in assets:
            asset["_id"] = str(asset["_id"])

        return assets