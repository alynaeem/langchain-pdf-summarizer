import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()
API_KEY = os.getenv("API_KEY")


def load_google_genai_model():
    try:
        return GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=API_KEY)
    except Exception as e:
        print(f"Error loading Google Generative AI model: {e}")
        return None