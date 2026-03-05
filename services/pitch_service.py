"""Sales pitch generation service."""

from services.groq_service import call_groq
from utils.prompt_builder import build_pitch_prompt
from utils.response_formatter import format_response


def generate_pitch(
    product: str, persona: str, industry: str, company_size: str, budget: str
) -> dict:
    """Generate a complete sales pitch package using AI.

    Args:
        product: Product or solution name.
        persona: Customer persona description.
        industry: Target industry.
        company_size: Size of the target company.
        budget: Budget range of the prospect.

    Returns:
        Formatted pitch data dictionary.
    """
    system_prompt, user_prompt = build_pitch_prompt(
        product, persona, industry, company_size, budget
    )
    raw = call_groq(system_prompt, user_prompt)
    result = format_response(raw)
    result["industry"] = industry
    return result
