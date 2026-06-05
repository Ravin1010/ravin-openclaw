from fastapi import APIRouter

from backend.app.models.chat_models import (
    ChatRequest,
    ChatResponse
)

from backend.app.services.chat_service import process_chat


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = process_chat(
        request.session_id,
        request.message
    )

    return result