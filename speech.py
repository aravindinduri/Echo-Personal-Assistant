# import os
# import speech_recognition as sr
# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play

# def speak(text, lang='en'):
#     """Convert text to speech and play it."""
#     try:
#         echo_text = f"{text}."
#         tts = gTTS(text=echo_text, lang=lang)
#         mp3_file = "/tmp/buddy_response.mp3"
#         tts.save(mp3_file)
#         sound = AudioSegment.from_mp3(mp3_file)
#         wav_file = "/tmp/buddy_response.wav"
#         faster_sound = sound.speedup(playback_speed=1.35)
#         faster_sound.export(wav_file, format="wav")
#         play(AudioSegment.from_wav(wav_file))
#         os.remove(mp3_file)
#         os.remove(wav_file)
#     except Exception as e:
#         print(f"⚠️ Audio Error: {e}")
#         print("\a") 

# def recognize_speech():
#     """Recognize speech input and convert it to text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Speak your command:")
#         recognizer.adjust_for_ambient_noise(source)
#         try:
#             audio = recognizer.listen(source, timeout=10)
#         except sr.WaitTimeoutError:
#             speak("I didn't hear anything. Please try again.")
#             return None
#     try:
#         command = recognizer.recognize_google(audio).lower()
#         speak(f"I heard: {command}")
#         return command
#     except sr.UnknownValueError:
#         speak("I didn't catch that. Could you please repeat?")
#         return None
#     except sr.RequestError:
#         speak("My speech service is currently unavailable.")
#         return None


# import os
# import wave
# import pyaudio
# import numpy as np
# import noisereduce as nr
# import soundfile as sf
# from scipy.signal import butter, lfilter
# import speech_recognition as sr
# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play

# RATE = 16000
# CHANNELS = 1
# FORMAT = pyaudio.paInt16
# CHUNK = 1024
# NOISE_SAMPLE_DURATION = 2
# AUDIO_FILE = "recorded_audio.wav"
# CLEANED_AUDIO_FILE = "cleaned_audio.wav"

# def butter_bandpass(lowcut, highcut, fs, order=4):
#     nyquist = 0.5 * fs
#     low = lowcut / nyquist
#     high = highcut / nyquist
#     b, a = butter(order, [low, high], btype="band")
#     return b, a

# def apply_bandpass_filter(audio, lowcut=300, highcut=3000, fs=16000, order=4):
#     b, a = butter_bandpass(lowcut, highcut, fs, order)
#     return lfilter(b, a, audio)

# def recognize_speech():
#     """Record audio, process noise reduction, and recognize speech."""
#     speak("Recording background noise. Please stay silent.")
#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#     noise_frames = [stream.read(CHUNK) for _ in range(0, int(RATE / CHUNK * NOISE_SAMPLE_DURATION))]
#     speak("Now speak your command.")
    
#     voice_frames = [stream.read(CHUNK) for _ in range(0, int(RATE / CHUNK * 5))]  

#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

#     with wave.open(AUDIO_FILE, "wb") as wf:
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(audio.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b"".join(voice_frames))

#     data, samplerate = sf.read(AUDIO_FILE)
#     noise_array = np.frombuffer(b"".join(noise_frames), dtype=np.int16)
#     reduced_noise = nr.reduce_noise(y=data, sr=samplerate, y_noise=noise_array, prop_decrease=0.8)
#     filtered_audio = apply_bandpass_filter(reduced_noise, lowcut=300, highcut=3000, fs=samplerate)
#     sf.write(CLEANED_AUDIO_FILE, filtered_audio, samplerate)

#     recognizer = sr.Recognizer()
#     with sr.AudioFile(CLEANED_AUDIO_FILE) as source:
#         audio = recognizer.record(source)

#     try:
#         text = recognizer.recognize_google(audio)
#         speak(text)
#         return text
#     except sr.UnknownValueError:
#         speak("I couldn't understand. Please try again.")
#         return None
#     except sr.RequestError:
#         speak("Google Speech Recognition is unavailable.")
#         return None

# def speak(text, lang='en'):
#     """Convert text to speech and play it."""
#     tts = gTTS(text=text, lang=lang)
#     mp3_file = "/tmp/buddy_response.mp3"
#     tts.save(mp3_file)
#     sound = AudioSegment.from_mp3(mp3_file)
#     play(sound)
#     os.remove(mp3_file)

# if __name__ == "__main__":
#     recognize_speech(AUDIO_FILE) 

import os
import wave
import pyaudio
import numpy as np
import noisereduce as nr
import soundfile as sf
from scipy.signal import butter, lfilter
import speech_recognition as sr
from elevenlabs import generate, play, set_api_key , voices

# Set your ElevenLabs API key here
set_api_key(ELEVEN_LABS)

# available_voices = voices()
# print(available_voices)
# Audio settings
RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paInt16
CHUNK = 1024
NOISE_SAMPLE_DURATION = 2
AUDIO_FILE = "recorded_audio.wav"
CLEANED_AUDIO_FILE = "cleaned_audio.wav"

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype="band")
    return b, a

def apply_bandpass_filter(audio, lowcut=300, highcut=3000, fs=16000, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order)
    return lfilter(b, a, audio)

def recognize_speech():
    """Record, reduce noise, and recognize speech."""
    print("Recording background noise. Please stay silent.")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    noise_frames = [stream.read(CHUNK) for _ in range(0, int(RATE / CHUNK * NOISE_SAMPLE_DURATION))]
    speak("Now speak your command.")
    
    voice_frames = [stream.read(CHUNK) for _ in range(0, int(RATE / CHUNK * 5))]  

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(AUDIO_FILE, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(voice_frames))

    data, samplerate = sf.read(AUDIO_FILE)
    noise_array = np.frombuffer(b"".join(noise_frames), dtype=np.int16)
    reduced_noise = nr.reduce_noise(y=data, sr=samplerate, y_noise=noise_array, prop_decrease=0.8)
    filtered_audio = apply_bandpass_filter(reduced_noise, lowcut=300, highcut=3000, fs=samplerate)
    sf.write(CLEANED_AUDIO_FILE, filtered_audio, samplerate)

    recognizer = sr.Recognizer()
    with sr.AudioFile(CLEANED_AUDIO_FILE) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        speak(text)
        return text
    except sr.UnknownValueError:
        speak("I couldn't understand. Please try again.")
        return None
    except sr.RequestError:
        speak("Google Speech Recognition is unavailable.")
        return None

def speak(text, voice="George"):
    """Convert text to speech using ElevenLabs and play it."""
    try:
        audio = generate(text=text, voice=voice, model="eleven_multilingual_v2")
        play(audio)
    except Exception as e:
        print(f"⚠️ Speech Error: {e}")

if __name__ == "__main__":
    recognize_speech()
