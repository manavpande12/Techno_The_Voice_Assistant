import pyautogui
import time
from SpeakGet.Talk import speak

def ClickMe():
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(3)
    speak("ONE")
    speak("TWO")
    speak("THREE")
    speak("SMILE")
    pyautogui.press("enter")




