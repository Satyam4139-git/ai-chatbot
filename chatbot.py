from groq import Groq
import os

# Get API key from environment
# NO API KEY IN CODE!
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Store conversation history
conversation_history = []

def get_chatbot_response(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    system_prompt = """
    You are a helpful customer service
    assistant. You are friendly, polite
    and professional. Help users with
    their questions clearly and concisely.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            *conversation_history
        ],
        max_tokens=500,
        temperature=0.7
    )

    bot_response = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": bot_response
    })

    return bot_response

def clear_history():
    global conversation_history
    conversation_history = []
    return "Conversation cleared!"