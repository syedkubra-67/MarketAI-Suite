"""Prompt construction utilities for each AI module."""


def build_campaign_prompt(product: str, audience: str, platform: str) -> tuple[str, str]:
    """Build system and user prompts for marketing campaign generation.

    Returns:
        A tuple of (system_prompt, user_prompt).
    """
    system_prompt = (
        "You are an expert marketing strategist. You create data-driven, creative, "
        "and actionable marketing campaigns. Always respond with well-structured, "
        "professional content formatted in clear sections. Use markdown formatting."
    )

    user_prompt = f"""Create a comprehensive marketing campaign for the following:

**Product/Service:** {product}
**Target Audience:** {audience}
**Marketing Platform:** {platform}

Please provide the following in your response:

## Campaign Objectives
List 3-5 clear, measurable campaign objectives.

## Content Ideas
Provide exactly 5 creative marketing content ideas with brief descriptions.

## Ad Copy Variations
Write exactly 3 compelling ad copy variations, each with a headline and body.

## Call-to-Action
Provide a platform-specific call-to-action strategy for {platform}.

## Posting Recommendations
Include optimal posting schedule, frequency, and timing recommendations for {platform}.

Make the content professional, engaging, and ready for immediate business use."""

    return system_prompt, user_prompt


def build_pitch_prompt(
    product: str, persona: str, industry: str, company_size: str, budget: str
) -> tuple[str, str]:
    """Build system and user prompts for sales pitch generation.

    Returns:
        A tuple of (system_prompt, user_prompt).
    """
    system_prompt = (
        "You are an elite sales strategist and copywriter. You craft compelling, "
        "personalized sales pitches that convert prospects into customers. Always "
        "respond with well-structured, professional content formatted in clear "
        "sections. Use markdown formatting."
    )

    user_prompt = f"""Create a comprehensive sales pitch package for:

**Product/Solution:** {product}
**Customer Persona:** {persona}
**Industry:** {industry}
**Company Size:** {company_size}
**Budget Range:** {budget}

Please provide all of the following sections:

## 30-Second Elevator Pitch
A concise, compelling pitch that can be delivered in 30 seconds.

## Value Proposition
A clear statement of the unique value this solution provides.

## Key Differentiators
List 3-5 factors that set this solution apart from competitors.

## Pain-Point Solutions
Identify 3-4 common pain points for this persona and how the product solves each.

## Strategic Call-to-Action
A specific, actionable next step for the prospect.

## Email Pitch Template
A complete, ready-to-send email pitch (subject line + body).

## LinkedIn Outreach Message
A professional LinkedIn connection/InMail message template.

Make every section tailored to the {industry} industry and {persona} persona."""

    return system_prompt, user_prompt


def build_lead_scoring_prompt(
    name: str, budget: str, need: str, urgency: str, authority: str, notes: str
) -> tuple[str, str]:
    """Build system and user prompts for lead qualification and scoring.

    Returns:
        A tuple of (system_prompt, user_prompt).
    """
    system_prompt = (
        "You are an expert sales analyst specializing in lead qualification and "
        "scoring. You evaluate leads using the BANT framework (Budget, Authority, "
        "Need, Timeline/Urgency). Always respond with well-structured, professional "
        "content formatted in clear sections. Use markdown formatting."
    )

    user_prompt = f"""Evaluate and score the following sales lead:

**Lead Name:** {name}
**Budget:** {budget}
**Business Need:** {need}
**Urgency Level:** {urgency}
**Decision Authority:** {authority}
**Additional Notes:** {notes}

Please provide a thorough evaluation with the following:

## Lead Score
Provide a numeric score from 0 to 100. State it clearly as: **Score: XX/100**

## Lead Category
Based on the score, categorize as:
- 90-100: 🔥 Hot Lead
- 75-89: 🟠 Warm Lead
- 60-74: 🟡 Lukewarm Lead
- Below 60: 🔵 Cold Lead

State the category clearly.

## Detailed Evaluation
Analyze each BANT criterion:
- **Budget Strength:** Analysis of the budget adequacy
- **Need Relevance:** How well the need aligns with conversion potential
- **Urgency Assessment:** Timeline and urgency analysis
- **Authority Level:** Decision-making power evaluation

## Conversion Probability
Provide an estimated conversion probability as a percentage with reasoning.

## Recommended Next Steps
List 3-5 specific, actionable next steps for the sales team.

Be precise, data-driven, and actionable in your analysis."""

    return system_prompt, user_prompt
