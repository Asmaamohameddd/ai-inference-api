# Gemini AI Inference API

A simple **FastAPI**-based inference API using **Google Gemini API** for text generation.  
This project demonstrates:

- Receiving text input
- Calling the Gemini LLM API
- Returning structured JSON output
- Handling failures (timeouts, retries, rate limits, server errors)
- Logging token usage (prompt, completion, total tokens)
## Example Request

Endpoint: `POST /infer`

**Request Body:**
```json
{
  "prompt": "what is AI"
}
**Request**
{
  "output": "Artificial Intelligence (AI) is a broad field of computer science that focuses on creating machines capable of performing tasks that typically require human intelligence. In simpler terms, it's about making computers 'think' and 'reason' like humans, or even exceed human capabilities in certain areas...",
  "tokens_used": {}
}

