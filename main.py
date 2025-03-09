import asyncio
from conversation import conversation_loop
from speech import speak

async def main():
    """Start the Buddy Assistant conversation."""
    await conversation_loop()
    speak("All done! I'm always here if you need more help.")

if __name__ == "__main__":
    asyncio.run(main())
