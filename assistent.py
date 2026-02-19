import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set female voice (if available)
voices = engine.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand.")
        return ""

def open_browser(url):
    webbrowser.open(url)

def ai_assistant():
    speak("Hello Ravi, I am your AI Assistant")

    important_websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "amazon": "https://www.amazon.com",
        "flipkart": "https://www.flipkart.com",
        "twitter": "https://www.twitter.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://stackoverflow.com",
        "wikipedia": "https://www.wikipedia.org",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "drive": "https://drive.google.com",
        "netflix": "https://www.netflix.com",
        "hotstar": "https://www.hotstar.com",
        "spotify": "https://www.spotify.com",
        "telegram": "https://web.telegram.org",
        "whatsapp": "https://web.whatsapp.com",
        "snapchat": "https://www.snapchat.com",
        "pinterest": "https://www.pinterest.com",
        "quora": "https://www.quora.com",
        "reddit": "https://www.reddit.com",
        "udemy": "https://www.udemy.com",
        "coursera": "https://www.coursera.org",
        "geeksforgeeks": "https://www.geeksforgeeks.org",
        "w3schools": "https://www.w3schools.com",
        "hackerrank": "https://www.hackerrank.com",
        "leetcode": "https://www.leetcode.com",
        "codechef": "https://www.codechef.com",
        "kaggle": "https://www.kaggle.com",
        "medium": "https://medium.com",
        "news": "https://news.google.com",
        "bbc": "https://www.bbc.com",
        "cnn": "https://www.cnn.com",
        "nytimes": "https://www.nytimes.com",
        "espn": "https://www.espn.com",
        "weather": "https://weather.com",
        "booking": "https://www.booking.com",
        "airbnb": "https://www.airbnb.com",
        "irctc": "https://www.irctc.co.in",
        "ola": "https://www.olacabs.com",
        "uber": "https://www.uber.com",
        "zomato": "https://www.zomato.com",
        "swiggy": "https://www.swiggy.com",
        "paytm": "https://www.paytm.com",
        "phonepe": "https://www.phonepe.com",
        "groww": "https://www.groww.in",
        "zerodha": "https://www.zerodha.com",
        "canva": "https://www.canva.com",
        "removebg": "https://www.remove.bg",
        "pixabay": "https://www.pixabay.com",
        "unsplash": "https://www.unsplash.com",
        "freepik": "https://www.freepik.com",
        "adobe": "https://www.adobe.com",
        "notion": "https://www.notion.so",
        "trello": "https://www.trello.com",
        "slack": "https://www.slack.com",
        "zoom": "https://www.zoom.us",
        "skype": "https://www.skype.com",
        "discord": "https://www.discord.com",
        "imdb": "https://www.imdb.com",
        "prime video": "https://www.primevideo.com",
        "oracle": "https://www.oracle.com",
        "microsoft": "https://www.microsoft.com",
        "apple": "https://www.apple.com",
        "samsung": "https://www.samsung.com",
        "nasa": "https://www.nasa.gov",
        "tesla": "https://www.tesla.com",
        "yahoo": "https://www.yahoo.com",
        "bing": "https://www.bing.com",
        "duckduckgo": "https://duckduckgo.com",
        "translate": "https://translate.google.com",
        "maps": "https://maps.google.com",
        "calendar": "https://calendar.google.com",
        "meet": "https://meet.google.com",
        "dropbox": "https://www.dropbox.com",
        "mega": "https://mega.io",
        "gitlab": "https://gitlab.com",
        "bitbucket": "https://bitbucket.org",
        "digitalocean": "https://www.digitalocean.com",
        "heroku": "https://www.heroku.com",
        "openai": "https://www.openai.com",
        "khan academy": "https://www.khanacademy.org",
        "byjus": "https://byjus.com",
        "unacademy": "https://unacademy.com",
        "vedantu": "https://www.vedantu.com",
        "physics wallah": "https://www.pw.live",
        "gate overflow": "https://gateoverflow.in"
    }

    while True:
        command = listen()

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "open" in command:
            found = False
            for site in important_websites:
                if site in command:
                    open_browser(important_websites[site])
                    speak(f"Opening {site}")
                    found = True
                    break
            if not found:
                speak("Website not found in my list")

        elif "search" in command:
            query = command.replace("search", "").strip()
            open_browser(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")

        elif "exit" in command or "bye" in command or "quit" in command:
            speak("Goodbye Ravi")
            break

        else:
            speak("Please say a valid command")

if __name__ == "__main__":
    ai_assistant()
