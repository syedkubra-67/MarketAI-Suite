"""Lead qualification and scoring service."""

from services.groq_service import call_groq
from utils.prompt_builder import build_lead_scoring_prompt
from utils.response_formatter import format_response, extract_score, get_lead_category


def score_lead(
    name: str, budget: str, need: str, urgency: str, authority: str, notes: str
) -> dict:
    """Evaluate and score a sales lead using AI.

    Args:
        name: Lead name or company name.
        budget: Available budget information.
        need: Business need description.
        urgency: Urgency level.
        authority: Decision-making authority.
        notes: Additional notes about the lead.

    Returns:
        Formatted lead scoring data with score, category, and analysis.
    """
    system_prompt, user_prompt = build_lead_scoring_prompt(
        name, budget, need, urgency, authority, notes
    )
    raw = call_groq(system_prompt, user_prompt)
    result = format_response(raw)

    # Extract numeric score and category
    score = extract_score(raw)
    if score is not None:
        result["score"] = score
        result["category"] = get_lead_category(score)
    else:
        result["score"] = None
        result["category"] = {"label": "Unable to Score", "emoji": "❓", "color": "#6b7280"}

    result["lead_name"] = name
    return result
