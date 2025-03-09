import os
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def speak(text, lang='en'):
    """Convert text to speech and play it."""
    try:
        echo_text = f"{text}."
        tts = gTTS(text=echo_text, lang=lang)
        mp3_file = "/tmp/buddy_response.mp3"
        tts.save(mp3_file)
        sound = AudioSegment.from_mp3(mp3_file)
        wav_file = "/tmp/buddy_response.wav"
        faster_sound = sound.speedup(playback_speed=1.35)
        faster_sound.export(wav_file, format="wav")
        play(AudioSegment.from_wav(wav_file))
        os.remove(mp3_file)
        os.remove(wav_file)
    except Exception as e:
        print(f"⚠️ Audio Error: {e}")
        print("\a") 

def recognize_speech():
    """Recognize speech input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak your command:")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None
    try:
        command = recognizer.recognize_google(audio).lower()
        speak(f"I heard: {command}")
        return command
    except sr.UnknownValueError:
        speak("I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError:
        speak("My speech service is currently unavailable.")
        return None
