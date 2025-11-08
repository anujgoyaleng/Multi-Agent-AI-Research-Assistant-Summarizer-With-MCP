"""
LLM Configuration Module
Initializes and provides Google Gemini AI instance
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    """
    Initialize and return Google Gemini LLM instance
    
    Returns:
        ChatGoogleGenerativeAI: Configured Gemini AI instance
    """
    api_key = os.getenv("api_key")
    if not api_key:
        raise ValueError("API key not found. Please set 'api_key' in your .env file")
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=api_key,
        temperature=0.7
    )