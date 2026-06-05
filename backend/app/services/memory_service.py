from backend.app.memory.conversation_memory import (
    append_message,
    get_conversation
)


def save_message(session_id, role, content):
    append_message(session_id, role, content)


def load_conversation(session_id):
    return get_conversation(session_id)