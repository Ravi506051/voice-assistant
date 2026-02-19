import pyttsx3
import speech_recognition as sr
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set a female voice (if available)
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Function to make the chatbot speak
def speak(text):
    print(f"Chatbot: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print(f"You: {user_input}")
            return user_input.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

# Simple chatbot responses
responses = [
    "Hello! How can I help you today?",
    "Nice to meet you! What's on your mind?",
    "I'm here to assist you. What do you need?",
    "How can I make your day better?",
    "Tell me more about what you're thinking."
]

# Main chatbot loop
def chatbot():
    speak("Hi! I'm Muskan. How can I assist you today?")
    while True:
        user_input = listen()
        if user_input:
            if "exit" in user_input or "bye" in user_input:
                speak("Goodbye! Have a great day!")
                break
            else:
                response = random.choice(responses)
                speak(response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
