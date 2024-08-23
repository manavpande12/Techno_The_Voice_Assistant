from pynput.keyboard import Key,Controller
import pyautogui
from SpeakGet.Talk import speak
import pygetwindow as gw
from time import sleep

keyboard = Controller()



def is_youtube_playing():
    active_window = gw.getActiveWindow()
    if active_window is not None:
        if "YouTube" in active_window.title:
            return True
    return False

def volumeup():
    speak("Turning volume up,sir")
    for i in range(10):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    speak("Turning volume down, sir")
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


def play():
    if is_youtube_playing():
        pyautogui.press("k")
        speak("Video played")
    else:
        speak("No video is playing.")

def pause():
    if is_youtube_playing():
        pyautogui.press("k")
        speak("Video paused")
    else:
        speak("No video is playing.")

def mute():
    if is_youtube_playing():
        pyautogui.press("m")
        speak("Video muted")
    else:
        speak("No video is playing.")

def unmute():
    if is_youtube_playing():
        pyautogui.press("m")
        speak("Video unmuted")
    else:
        speak("No video is playing.")

def fulls():
    if is_youtube_playing():
        pyautogui.press("f")
        speak("Video fullscreened")
    else:
        speak("No video is playing.")

def nfulls():
    if is_youtube_playing():
        pyautogui.press("f")
        speak("Fullscreen exited")
    else:
        speak("No video is playing.")

def sub():
    if is_youtube_playing():
        pyautogui.press("c")
        speak("Subtitles are on")
    else:
        speak("No video is playing.")

def unsub():
    if is_youtube_playing():
        pyautogui.press("c")
        speak("Subtitles are off")
    else:
        speak("No video is playing.")

def rewind():
    if is_youtube_playing():
        pyautogui.press("j")
        speak("Rewinding 10 seconds")
    else:
        speak("No video is playing.")

def fast_forward():
    if is_youtube_playing():
        pyautogui.press("l")
        speak("Fast forwarding 10 seconds")
    else:
        speak("No video is playing.")

def go_to_beginning():
    if is_youtube_playing():
        pyautogui.press("home")
        speak("Going to the beginning of the video")
    else:
        speak("No video is playing.")

def go_to_end():
    if is_youtube_playing():
        pyautogui.press("end")
        speak("Going to the end of the video")
    else:
        speak("No video is playing.")
    