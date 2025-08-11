import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file and read the API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Create a chat session
chat = genai.GenerativeModel("gemini-2.0-flash").start_chat()

print("Gemini Chat is ready! Type 'exit' to end.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        break
    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("Error:", e)
