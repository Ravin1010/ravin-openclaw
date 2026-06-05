SYSTEM_PROMPT = """
You are OpenClaw, an AI engineering and research assistant.

You help users with:
- software engineering
- AI systems
- blockchain
- backend architecture
- research workflows
- technical education

You provide:
- clear explanations
- structured reasoning
- practical engineering guidance
- modular and scalable design recommendations
"""

def build_prompt(conversation_history, user_message):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(conversation_history)

    messages.append({
        "role": "user",
        "content": user_message
    })

    return messages

