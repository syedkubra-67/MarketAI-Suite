"""Routes for sales pitch generation."""

from flask import Blueprint, request, jsonify
from services.pitch_service import generate_pitch

pitch_bp = Blueprint("pitch", __name__)


@pitch_bp.route("/generate-pitch", methods=["POST"])
def generate_pitch_route():
    """Handle POST requests to generate a sales pitch.

    Expects form data or JSON with: product, persona, industry, company_size, budget.
    Returns JSON with the generated pitch content.
    """
    try:
        data = request.get_json() if request.is_json else request.form

        product = data.get("product", "").strip()
        persona = data.get("persona", "").strip()
        industry = data.get("industry", "").strip()
        company_size = data.get("company_size", "").strip()
        budget = data.get("budget", "").strip()

        # Validate required fields
        if not product:
            return jsonify({"error": "Product/solution name is required."}), 400
        if not persona:
            return jsonify({"error": "Customer persona is required."}), 400
        if not industry:
            return jsonify({"error": "Industry is required."}), 400

        result = generate_pitch(product, persona, industry, company_size, budget)
        return jsonify({"success": True, "data": result})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
