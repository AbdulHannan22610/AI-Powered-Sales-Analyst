import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ALLAM_MODEL = "allam-2-7b"
MAX_TOKENS_PER_PROMPT = int(os.getenv("MAX_TOKENS_PER_PROMPT", "500"))