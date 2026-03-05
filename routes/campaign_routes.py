"""Routes for marketing campaign generation."""

from flask import Blueprint, request, jsonify
from services.campaign_service import generate_campaign

campaign_bp = Blueprint("campaign", __name__)


@campaign_bp.route("/generate-campaign", methods=["POST"])
def generate_campaign_route():
    """Handle POST requests to generate a marketing campaign.

    Expects form data or JSON with: product, audience, platform.
    Returns JSON with the generated campaign content.
    """
    try:
        data = request.get_json() if request.is_json else request.form

        product = data.get("product", "").strip()
        audience = data.get("audience", "").strip()
        platform = data.get("platform", "").strip()

        # Validate required fields
        if not product:
            return jsonify({"error": "Product/service description is required."}), 400
        if not audience:
            return jsonify({"error": "Target audience is required."}), 400
        if not platform:
            return jsonify({"error": "Marketing platform is required."}), 400

        result = generate_campaign(product, audience, platform)
        return jsonify({"success": True, "data": result})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
