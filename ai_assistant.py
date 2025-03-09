from langchain_google_genai import ChatGoogleGenerativeAI
from config import API_KEY

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=API_KEY)

def ask_gemini(prompt):
    """Send a prompt to the Gemini AI model and return the response."""
    return llm.invoke(prompt).content

def parse_executable_command(response):
    """Extract an executable command from Gemini's response."""
    if "COMMAND:" in response:
        return response.split("COMMAND:")[-1].strip()
    return None
