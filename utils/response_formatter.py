"""Utilities for formatting and sanitizing AI responses."""

import re


def format_response(raw_text: str) -> dict:
    """Format a raw AI text response into a structured dictionary.

    Args:
        raw_text: The raw text response from the AI model.

    Returns:
        A dictionary with 'content' (the cleaned text) and 'sections'
        (a list of extracted section headings).
    """
    if not raw_text:
        return {"content": "", "sections": []}

    # Extract section headings
    sections = re.findall(r"^##\s+(.+)$", raw_text, re.MULTILINE)

    return {
        "content": raw_text.strip(),
        "sections": sections,
    }


def extract_score(raw_text: str) -> int | None:
    """Extract a numeric lead score from the AI response.

    Looks for patterns like 'Score: 85/100' or '**Score: 85/100**'.

    Args:
        raw_text: The raw text response from the AI model.

    Returns:
        The extracted integer score, or None if not found.
    """
    patterns = [
        r"\*?\*?Score:\s*(\d+)\s*/\s*100\*?\*?",
        r"Lead\s+Score[:\s]+(\d+)",
        r"(\d+)\s*/\s*100",
    ]

    for pattern in patterns:
        match = re.search(pattern, raw_text, re.IGNORECASE)
        if match:
            score = int(match.group(1))
            if 0 <= score <= 100:
                return score

    return None


def get_lead_category(score: int) -> dict:
    """Determine lead category based on the numeric score.

    Args:
        score: The lead score from 0 to 100.

    Returns:
        A dictionary with 'label', 'emoji', and 'color' keys.
    """
    if score >= 90:
        return {"label": "Hot Lead", "emoji": "🔥", "color": "#ef4444"}
    elif score >= 75:
        return {"label": "Warm Lead", "emoji": "🟠", "color": "#f97316"}
    elif score >= 60:
        return {"label": "Lukewarm Lead", "emoji": "🟡", "color": "#eab308"}
    else:
        return {"label": "Cold Lead", "emoji": "🔵", "color": "#3b82f6"}
