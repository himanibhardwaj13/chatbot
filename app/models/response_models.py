
from typing import Any
from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    question: str
    response: dict[str, Any]