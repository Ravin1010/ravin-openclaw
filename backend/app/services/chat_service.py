from backend.app.services.memory_service import (
    save_message,
    load_conversation
)

from backend.app.services.prompt_service import build_prompt

from backend.app.services.llm_service import generate_response

from backend.app.memory.session_manager import create_session_id


def process_chat(session_id, user_message):

    # Create new session if none provided
    if not session_id:
        session_id = create_session_id()

    # Save user message
    save_message(session_id, "user", user_message)

    # Load updated conversation
    conversation_history = load_conversation(session_id)

    # Build prompt/messages
    messages = build_prompt(
        conversation_history,
        user_message
    )

    # Generate AI response
    assistant_response = generate_response(messages)

    # Save assistant response
    save_message(
        session_id,
        "assistant",
        assistant_response
    )

    return {
        "session_id": session_id,
        "response": assistant_response
    }