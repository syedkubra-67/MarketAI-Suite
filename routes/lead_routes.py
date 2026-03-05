"""Routes for lead qualification and scoring."""

from flask import Blueprint, request, jsonify
from services.lead_service import score_lead

lead_bp = Blueprint("lead", __name__)


@lead_bp.route("/score-lead", methods=["POST"])
def score_lead_route():
    """Handle POST requests to score a sales lead.

    Expects form data or JSON with: name, budget, need, urgency, authority, notes.
    Returns JSON with the lead score, category, and analysis.
    """
    try:
        data = request.get_json() if request.is_json else request.form

        name = data.get("name", "").strip()
        budget = data.get("budget", "").strip()
        need = data.get("need", "").strip()
        urgency = data.get("urgency", "").strip()
        authority = data.get("authority", "").strip()
        notes = data.get("notes", "").strip()

        # Validate required fields
        if not name:
            return jsonify({"error": "Lead name is required."}), 400
        if not budget:
            return jsonify({"error": "Budget information is required."}), 400
        if not need:
            return jsonify({"error": "Business need is required."}), 400
        if not urgency:
            return jsonify({"error": "Urgency level is required."}), 400
        if not authority:
            return jsonify({"error": "Decision authority is required."}), 400

        result = score_lead(name, budget, need, urgency, authority, notes)
        return jsonify({"success": True, "data": result})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
