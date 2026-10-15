import requests

from config import ALLAM_MODEL, GROQ_API_KEY, MAX_TOKENS_PER_PROMPT

API_URL = "https://api.groq.com/openai/v1/chat/completions"


def ask_allam(question, context):
    if not GROQ_API_KEY:
        return "ALLaM API key missing. Add GROQ_API_KEY to your .env file."

    payload = {
        "model": ALLAM_MODEL,
        "max_tokens": MAX_TOKENS_PER_PROMPT,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a sales analyst AI. "
                    f"Reply in at most {MAX_TOKENS_PER_PROMPT} tokens. Be very brief."
                ),
            },
            {"role": "user", "content": f"DATA:\n{context}\nQUESTION:\n{question}"},
        ],
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
            timeout=60,
        )
    except requests.Timeout:
        return "ALLaM API request timed out. Please try again."
    except requests.RequestException:
        return "Could not reach the ALLaM API. Check your connection and try again."

    if response.status_code == 401:
        return "ALLaM API authentication failed. Check GROQ_API_KEY in your .env file."
    if response.status_code == 403:
        return "ALLaM API access denied. Check your API key permissions."
    if response.status_code == 429:
        return "ALLaM API rate limit reached. Please try again shortly."
    if response.status_code == 404:
        return f"ALLaM model '{ALLAM_MODEL}' is unavailable."
    if response.status_code >= 500:
        return "ALLaM API is temporarily unavailable. Please try again later."
    if not response.ok:
        return f"ALLaM API returned an error (HTTP {response.status_code}). Check your request."

    try:
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError, TypeError):
        return "ALLaM API returned an unexpected response. Please try again."

    if not isinstance(answer, str) or not answer.strip():
        return "ALLaM API returned an empty response. Please try again."

    return answer
