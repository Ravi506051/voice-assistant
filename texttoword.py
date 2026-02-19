from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Opens the audio file

text = "Hello! This is a natural voice text-to-speech converter."
text_to_speech(text)
