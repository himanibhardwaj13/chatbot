from fastapi import APIRouter
from app.graph.graph import graph_builder
from app.models.response_models import ChatRequest, ChatResponse


router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):

    result = await graph_builder.ainvoke({
        "question": request.question
    })

    return result["response"]
