# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from ai_client import call_llm
from utils import log_token_usage

# -----------------------
# App & Limiter
# -----------------------
app = FastAPI(title="Gemini AI Inference API")

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# 🔴 THIS LINE WAS MISSING (CRITICAL)
app.add_middleware(SlowAPIMiddleware)

# -----------------------
# Rate limit error handler
# -----------------------
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded. Try again later."}
    )

# -----------------------
# Root endpoint
# -----------------------
@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

# -----------------------
# Models
# -----------------------
class InferenceRequest(BaseModel):
    prompt: str

class InferenceResponse(BaseModel):
    output: str
    tokens_used: dict

# -----------------------
# Inference endpoint
# -----------------------
@app.post("/infer", response_model=InferenceResponse)
@limiter.limit("5/minute")
async def infer(request: Request, body: InferenceRequest):
    try:
        output, token_info = await call_llm(body.prompt)
        log_token_usage(body.prompt, output, token_info)
        return {
            "output": output,
            "tokens_used": token_info
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
