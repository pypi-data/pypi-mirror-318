def Gemini_Response(system_instruction=None):
    if system_instruction is None:
        system_instruction = "You are a helpful, friendly, and concise chatbot designed to assist users by providing clear, accurate, and relevant information."
    
    return f"""
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

##Gemini
api_key_gemini = os.getenv("GOOGLE_API_KEY")
if not api_key_gemini:
    raise ValueError("API key for Google Generative AI is not set in the environment variables.")


genai.configure(api_key=api_key_gemini)

generation_config = {{
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 100,
    "response_mime_type": "text/plain",
}}


instruction = "{system_instruction}"


gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=instruction
)


chat_session_gemini = gemini.start_chat(history=[])

def get_gemini_response(prompt):
    try:
        response  = chat_session_gemini.send_message(prompt)
        return response.text
    except Exception as e:
        return "Oops! it seems I didn't get your question"
"""
