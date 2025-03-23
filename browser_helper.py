from browser_use import Agent, Browser, BrowserConfig
from config import API_KEY, CHROME_PATH
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=API_KEY)

browser = Browser(config=BrowserConfig(chrome_instance_path=CHROME_PATH))

async def search_web(query):
    """Perform a web search using the browser."""
    agent = Agent(task=f"Search the web for: {query}", llm=llm, browser=browser)
    result = await agent.run()
    await browser.close()
    return result
