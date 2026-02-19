import ollama
import speech_recognition as sr
import pyttsx3
import pywhatkit
import smtplib
import datetime
import webbrowser
import json
import os

# ========== VOICE ENGINE ==========
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ========== VOICE INPUT ==========
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# ========== LLM INTENT DETECTOR ==========
def detect_intent(command):

    system_prompt = """
    You are an AI assistant.
    Identify the user's intent and return JSON only.

    Possible intents:
    - send_email
    - send_whatsapp
    - youtube_search
    - make_call
    - open_website
    - get_time
    - general_chat

    Return format:
    {
      "intent": "intent_name",
      "details": "important information extracted"
    }
    """

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": command}
        ]
    )

    try:
        return json.loads(response['message']['content'])
    except:
        return {"intent": "general_chat", "details": command}

# ========== EMAIL FUNCTION ==========
def send_email(content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_app_password")
    server.sendmail("your_email@gmail.com", "receiver@gmail.com", content)
    server.quit()

# ========== MAIN ASSISTANT ==========
def assistant():

    speak("Hello Ravi, your smart AI assistant is ready")

    while True:

        command = listen()

        if command == "":
            continue

        if "exit" in command:
            speak("Goodbye Ravi")
            break

        intent_data = detect_intent(command)

        intent = intent_data["intent"]
        details = intent_data["details"]

        # ---- INTENT ROUTING ----

        if intent == "send_email":
            speak("Writing and sending email")
            send_email(details)
            speak("Email sent successfully")

        elif intent == "send_whatsapp":
            speak("Sending WhatsApp message")
            pywhatkit.sendwhatmsg_instantly("+91XXXXXXXXXX", details)
            speak("Message sent")

        elif intent == "youtube_search":
            speak("Searching on YouTube")
            pywhatkit.playonyt(details)

        elif intent == "make_call":
            number = "XXXXXXXXXX"
            os.system(f"adb shell am start -a android.intent.action.CALL -d tel:{number}")
            speak("Calling now")

        elif intent == "open_website":
            webbrowser.open("https://" + details)
            speak("Opening website")

        elif intent == "get_time":
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        else:
            reply = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": command}]
            )
            speak(reply['message']['content'])

if __name__ == "__main__":
    assistant()
