import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Get Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )

# Create Groq client
client = Groq(api_key=groq_api_key)


# =========================================================
# SMARTBUDDY PERSONALITY
# =========================================================

SYSTEM_INSTRUCTION = """
You are SmartBuddy AI, a friendly personal AI assistant.

User's name:
Satya

Personality:
- Very friendly and helpful
- Understand Hinglish naturally
- Reply in simple Hinglish when appropriate
- Be practical and concise
- Explain technical concepts step-by-step
- Help with coding, DSA, studies, projects and everyday questions
- Remember information from the current conversation
- If the user asks something unclear, ask a short clarification
- Talk naturally like a helpful AI buddy

For study questions:
- Explain concepts clearly
- Give examples
- Use simple language
- Help the user understand instead of only giving the answer

For coding questions:
- Give clean and optimized code
- Explain the code
- Mention important mistakes when necessary
"""


# =========================================================
# CONVERSATION MEMORY
# =========================================================

messages = [
    {
        "role": "system",
        "content": SYSTEM_INSTRUCTION
    }
]


# =========================================================
# ASK SMARTBUDDY
# =========================================================

def ask_ai(user_message):
    """
    Send a message to SmartBuddy and return the AI response.
    """

    try:

        # Add user's message
        messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # Ask Groq
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=0.7,
            max_completion_tokens=2048,
        )

        # Get AI response
        assistant_message = response.choices[0].message.content

        # Save AI response to conversation history
        messages.append(
            {
                "role": "assistant",
                "content": assistant_message
            }
        )

        return assistant_message

    except Exception as e:

        # Remove failed user message
        if messages and messages[-1]["role"] == "user":
            messages.pop()

        return f"⚠️ SmartBuddy error: {e}"