import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("base_url"),
    api_key=os.getenv("OPENROUTER_API_KEY")
)

chat_history = []

print("AI Chatbot Initialized. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "exit":
        print("Goodbye!")
        break
        
    if not user_input.strip():
        continue

    chat_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=chat_history
        )
        
        bot_reply = response.choices[0].message.content
        print(f"\nBot: {bot_reply}\n")
        
        chat_history.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
