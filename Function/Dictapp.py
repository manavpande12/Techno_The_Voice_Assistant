import os 
import pyautogui
import webbrowser
from SpeakGet.Talk import speak
import subprocess


dictapp = {
    "cmd": "cmd",
    "brave": "brave",
    "spotify": "spotify",
    "discord": "discord"
}


def openappweb(query):
    if ".com" in query or ".co.in" in query or ".org" in query or ".nf" in query:
        webbrowser.open(f"https://www.{query}")
    else:
        for app, command in dictapp.items():
                if app in query.lower():
                    speak(f"Launching {app}")
                    os.system(f"start {command}")
                    break
        else:
            speak("Application not found")

def closeappweb(query):
    # Application handling
    query = query.lower()
    for app, command in dictapp.items():
        if app in query:
            speak(f"Closing {app}")
            # Check if application is running
            result = subprocess.run(f"tasklist /FI \"IMAGENAME eq {command}.exe\"", shell=True, capture_output=True, text=True)
            if command not in result.stdout:
                speak(f"{app} is not running")
            else:
                subprocess.run(f"taskkill /f /im {command}.exe", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                speak(f"{app} closed")
            return
    speak("Application not found")



