# import asyncio
# from speech import speak, recognize_speech
# from ai_assistant import ask_gemini, parse_executable_command
# from browser_helper import search_web
# from command_executor import execute_command

# async def conversation_loop():
#     """Main assistant conversation loop."""
#     conversation_history = [
#         {
#             "role": "system",
#             "content": (
#                 "You are Echo, a Linux-based personal assistant. Answer questions clearly and helpfully. "
#                 "If a user asks a general question (e.g., 'Who is the Prime Minister of India?'), provide a direct, friendly answer. "
#                 "If the user instructs you to 'play' or 'execute' something, generate a valid one-line Ubuntu command. "
#                 "If the user's command contains 'browse', treat it as a web search request and provide a command to launch a search."
#                 "When generating terminal commands, output only the command on one line prefixed with 'COMMAND:' (with no extra commentary). don't use totem"
#             )
#         }
#     ]
    
#     speak("Hi there! I'm Echo. How can I assist you today?")
    
#     mode = ""
#     while mode not in ["text", "voice"]:
#         mode = input("Select input mode ('text' or 'voice'): ").lower()

#     while True:
#         user_input = input("📝 Enter your command: ") if mode == "text" else recognize_speech()
#         if not user_input:
#             continue

#         if user_input.strip().lower() in ["exit", "quit", "bye"]:
#             speak("Goodbye! See you next time.")
#             break

#         if "browse" in user_input:
#             query = user_input.replace("browse", "").strip()
#             speak("Opening up the web for you...")
#             print("🌍 Initiating browser search...")
#             result = await search_web(query)
#             speak("I've completed the web search.")
#             print(result)
#             continue

#         conversation_history.append({"role": "user", "content": user_input})
#         prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history])
#         gemini_response = ask_gemini(prompt)

#         if not gemini_response:
#             speak("I'm sorry, I didn't get a response. Could you please repeat?")
#             continue

#         conversation_history.append({"role": "assistant", "content": gemini_response})

#         command_to_execute = parse_executable_command(gemini_response)
        
#         if not command_to_execute:
#             speak(gemini_response)
        
#         print(f"Assistant: {gemini_response}")

#         if command_to_execute:
#             execute_command(command_to_execute)


import asyncio
from speech import speak, recognize_speech
from ai_assistant import ask_gemini, parse_executable_command
from browser_helper import search_web
from command_executor import execute_command
from file_search import load_json, find_file_path

JSON_FILE_PATH = "data.json"

APP_COMMANDS = {"open", "launch", "start", "run", "execute", "begin"}
MEDIA_COMMANDS = {"play", "watch", "stream"}
FILE_SEARCH_COMMANDS = {"find", "locate", "search for"}
BROWSER_COMMANDS = {"browse", "look up", "search online"}

async def conversation_loop():
    conversation_history = [
        {
            "role": "system",
          "content": (
                "You are Echo, a Linux-based personal assistant. Answer questions clearly and concisely. "
                "If a user instructs to 'play' a media file, search for it and generate a valid Ubuntu command. "
                "If the user instructs to 'open', 'run', or 'execute' an application, generate a command to launch the desktop application. "
                "If the user's command contains 'browse', 'look up', or 'search online', treat it as a web search request and output a command to launch a browser. "
                "If a user gives a command prefixed with 'control', assume it is related to controlling a mobile device via Vysor using ADB. "
                "Generate a valid ADB command (e.g., 'adb shell am start -n com.google.android.youtube/.HomeActivity') prefixed with 'COMMAND:' on one line. "
                "For example, if the user says 'control open youtube', generate a command to open YouTube on the mobile device. "
                "When generating terminal commands, output only the command prefixed with 'COMMAND:' on one line."
            )
        }
    ]
    
    speak("Hi there! I'm Echo. How can I assist you today?")
    
    mode = ""
    while mode not in ["text", "voice"]:
        mode = input("Select input mode ('text' or 'voice'): ").lower()
    
    json_data = load_json(JSON_FILE_PATH)
    
    while True:
        user_input = input("📝 Enter your command: ") if mode == "text" else recognize_speech()
        if not user_input:
            continue
        if user_input.strip().lower() in ["exit", "quit", "bye"]:
            speak("Goodbye! See you next time.")
            break

        if any(keyword in user_input for keyword in BROWSER_COMMANDS):
            query = user_input
            for keyword in BROWSER_COMMANDS:
                query = query.replace(keyword, "").strip()
            speak("Opening up the web for you...")
            print("🌍 Initiating browser search...")
            result = await search_web(query)
            speak("I've completed the web search.")
            print(result)
            continue

        conversation_history.append({"role": "user", "content": user_input})
        prompt = "\n".join(f"{msg['role']}: {msg['content']}" for msg in conversation_history)
        gemini_response = ask_gemini(prompt)
        if not gemini_response:
            speak("I'm sorry, I didn't get a response. Could you please repeat?")
            continue
        conversation_history.append({"role": "assistant", "content": gemini_response})
        print(f"Assistant: {gemini_response}")

        command_to_execute = parse_executable_command(gemini_response)
        if command_to_execute:
            if user_input.lower().startswith("control"):
                execute_command(command_to_execute)
            else:
                command_words = command_to_execute.split()
                if any(keyword in user_input for keyword in APP_COMMANDS):
                    execute_command(command_to_execute)
                elif any(keyword in user_input for keyword in MEDIA_COMMANDS):
                    filename_to_search = command_words[-1]
                    file_path = find_file_path(json_data, filename_to_search)
                    if file_path:
                        execute_command(command_to_execute, file_path)
                    else:
                        speak(f"File '{filename_to_search}' not found.")
                        print(f"❌ File '{filename_to_search}' not found in JSON.")
                elif any(keyword in user_input for keyword in FILE_SEARCH_COMMANDS):
                    filename_to_search = command_words[-1]
                    file_path = find_file_path(json_data, filename_to_search)
                    if file_path:
                        print(f"📂 File found: {file_path}")
                    else:
                        print(f"❌ File '{filename_to_search}' not found in JSON.")
                else:
                    execute_command(command_to_execute)
        else:
            speak(gemini_response)
