import os
from groq import AsyncGroq

API_KEY = os.environ.get("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set. Add it to your .env file.")

MODEL = "openai/gpt-oss-20b"

client = AsyncGroq(api_key=API_KEY)


async def call_claude(system_prompt: str, user_message: str) -> str:
    """
    Calls Groq API with a system + user prompt.
    Returns the text response.
    """
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=512,
        temperature=0.7
    )
    return response.choices[0].message.content
