# **Echo - Your Linux Personal Assistant** 🤖💬

**Echo** is a smart, Linux-based voice and text assistant powered by Google Gemini AI. It can perform various tasks such as answering general knowledge questions, executing system commands, performing web searches, controlling a phone remotely, and even speaking responses using text-to-speech technology.

## 🚀 **Features**

- 🎤 **Voice & Text Interaction** – Choose between voice input (speech recognition) or text input.
- 🤖 **Google Gemini AI** – Uses **Gemini 2.0 Flash** for intelligent responses.
- 🔍 **Web Search** – Automatically opens a browser and searches for information when requested.
- 🖥️ **Linux Command Execution** – Runs Ubuntu terminal commands based on user input.
- 📱 **Phone Control** – Control your Android phone remotely (send texts, make calls, check battery status, etc.).
- 🔊 **Text-to-Speech (TTS)** – Speaks responses in a friendly, natural tone.
- 🎧 **Speech Recognition** – Converts spoken words into text commands.

---

## 📂 **File Explanations**

| **File**              | **Description**                                           |
| --------------------- | --------------------------------------------------------- |
| `main.py`             | The entry point of the project. Starts the assistant.     |
| `config.py`           | Stores API keys and system configurations.                |
| `speech.py`           | Handles speech recognition and text-to-speech conversion. |
| `browser_helper.py`   | Manages web searches using a browser instance.            |
| `ai_assistant.py`     | Connects to Google Gemini AI and processes responses.     |
| `command_executor.py` | Runs and executes system commands in a new terminal.      |
| `phone_control.py`    | Manages remote phone control features.                    |
| `conversation.py`     | Manages user interactions and response handling.          |
| `file_data_generator.py` | Handles data file generation for processing.            |
| `requirements.txt`    | List of dependencies required for the project.            |
| `README.md`           | Documentation for the project.                            |

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository

```
git clone https://github.com/aravindinduri/Echo---Personal-Assistant
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Configure API Keys

```
API_KEY = "YOUR_GEMINI_API_KEY"
CHROME_PATH = ""
```

### 4️⃣ Run Echo Assistant

```
python3 main.py
```

---

## 🎤 How to Use

### Choose Input Mode:

- Type **"text"** to enter commands manually.
- Type **"voice"** to use voice commands.

### Give Commands:

#### General Queries:

```
Who is the Prime Minister of India?
```

#### Perform System Tasks:

```
Open VS Code
```

#### Search the Web:

```
Search for the latest AI trends
```

#### Control Your Phone:

```
Send a text to Mom: "Hey, I’ll be home soon."
Check my battery status.
Call John.
```

#### Exit the Assistant:

```
Say "exit", "quit", or "bye" to close the assistant.
```

---

## 🛠 Technologies Used

- **Python** 🐍 – Core language.
- **Google Gemini AI** 🤖 – AI-powered responses.
- **SpeechRecognition** 🎤 – Converts voice input into text.
- **gTTS (Google Text-to-Speech)** 🔊 – Generates speech responses.
- **Pydub** 🎵 – Adjusts and plays audio.
- **Browser Automation** 🌍 – Automates browser interactions.
- **Subprocess & OS** 💻 – Executes Linux commands.
- **Android Debug Bridge (ADB)** 📱 – Enables phone control features.

---

## 📌 Future Enhancements

- ✅ Improve natural conversation flow.
- ✅ Add support for more AI models.
- ✅ Integrate GUI interface.
- ✅ Enhance command execution safety.
- ✅ Expand phone control features (app control, notifications, etc.).

---

## 🎥 **Demo**
Watch the demo video here: [Demo Link](#)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

- Fork the repository.
- Create a feature branch.
- Make your changes and commit.
- Submit a pull request.

---

## 💡 Credits

Developed by **Aravind Induri**

For any inquiries, reach out at:
**[thearavindinduri@gmail.com](mailto:thearavindinduri@gmail.com)**

