from backend.app.memory.memory_store import memory_store


def initialize_session(session_id):
    if session_id not in memory_store:
        memory_store[session_id] = []


def append_message(session_id, role, content):
    initialize_session(session_id)

    memory_store[session_id].append({
        "role": role,
        "content": content
    })


def get_conversation(session_id):
    initialize_session(session_id)

    return memory_store[session_id]