from flask import Blueprint, request, jsonify

from app.assets.service import AssetService

asset_bp = Blueprint(
    "assets",
    __name__,
    url_prefix="/assets"
)


@asset_bp.route("/", methods=["POST"])
def create_asset():
    """
    Create Asset
    ---
    tags:
      - Assets

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object

          required:
            - device_name
            - asset_type
            - manufacturer
            - serial_number
            - assigned_to
            - department

          properties:

            device_name:
              type: string
              example: Dell Latitude 5440

            asset_type:
              type: string
              example: Laptop

            manufacturer:
              type: string
              example: Dell

            serial_number:
              type: string
              example: DL123456

            assigned_to:
              type: string
              example: Dhana

            department:
              type: string
              example: AI

            status:
              type: string
              example: Active

    responses:
      201:
        description: Asset Created
    """

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required."
        }), 400

    result = AssetService.create_asset(data)

    return jsonify(result), 201


@asset_bp.route("/", methods=["GET"])
def get_all_assets():
    """
    Get All Assets
    ---
    tags:
      - Assets

    responses:
      200:
        description: Asset List
    """

    assets = AssetService.get_all_assets()

    return jsonify({
        "success": True,
        "count": len(assets),
        "assets": assets
    }), 200