from groq import Groq
from config import Config


def call_groq(system_prompt: str, user_prompt: str) -> str:
    """Send a prompt to the Groq API and return the text response.

    Args:
        system_prompt: The system-level instruction for the AI model.
        user_prompt: The user-level message containing the specific request.

    Returns:
        The generated text response from the model.

    Raises:
        Exception: If the API call fails or the key is missing.
    """
    if not Config.GROQ_API_KEY or Config.GROQ_API_KEY == "YOUR_API_KEY":
        raise ValueError(
            "GROQ_API_KEY is not set. Please add your API key to the .env file."
        )

    client = Groq(api_key=Config.GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model=Config.GROQ_MODEL,
        temperature=0.7,
        max_tokens=4096,
    )

    return chat_completion.choices[0].message.content
