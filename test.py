import google.generativeai as palm
import os

api = os.getenv("MAKERSUITE_API_TOKEN")
palm.configure(api_key=api)

model = palm.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello, you are a chatbot who can educate me about various topics. Do not ask questions, just provide information."}
    ]
)
response = chat.send_message("Singapore")
print(response.text)