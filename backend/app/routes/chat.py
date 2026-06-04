from fastapi import APIRouter
from backend.app.models.chat_models import ChatRequest, ChatResponse
from backend.app.services.prompt_service import build_prompt
from backend.app.services.llm_service import generate_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    prompt = build_prompt(request.message)
    response = generate_response(prompt)

    return ChatResponse(response=response)