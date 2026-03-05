"""Campaign generation service."""

from services.groq_service import call_groq
from utils.prompt_builder import build_campaign_prompt
from utils.response_formatter import format_response


def generate_campaign(product: str, audience: str, platform: str) -> dict:
    """Generate a complete marketing campaign using AI.

    Args:
        product: Description of the product or service.
        audience: Target audience description.
        platform: Marketing platform (e.g., Instagram, LinkedIn).

    Returns:
        Formatted campaign data dictionary.
    """
    system_prompt, user_prompt = build_campaign_prompt(product, audience, platform)
    raw = call_groq(system_prompt, user_prompt)
    result = format_response(raw)
    result["platform"] = platform
    return result
