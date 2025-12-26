# ai_client.py
import os
from dotenv import load_dotenv
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash:generateContent"
)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(httpx.RequestError))
async def call_llm(prompt: str):
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    async with httpx.AsyncClient(timeout=10) as client:
        try:
            response = await client.post(GEMINI_API_URL, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            output = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            token_info = data.get("usage", {})
            return output, token_info
        except httpx.HTTPStatusError as e:
            raise Exception(f"LLM API returned {e.response.status_code}: {e.response.text}")
        except httpx.RequestError as e:
            raise Exception(f"LLM request failed: {e}")
