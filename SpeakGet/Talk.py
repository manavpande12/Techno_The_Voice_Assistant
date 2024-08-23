
from Recognisation.FastRecognisation import Listen
import re
import threading
from tkinter import *
import pyttsx3
import time
from Graphics.win import output_text,change_gif,app


def typing_animation(text, color, prefix):
    global output_text
    output_text.tag_config(color, foreground=color)
    output_text.insert(END, prefix, color)
    for char in text.title():
        output_text.insert(END, char)
        output_text.see(END)  # Scroll to the end of the text area
        output_text.update_idletasks()
        time.sleep(0.010)
    output_text.insert(END, "\n")
    output_text.see(END) 



def filter_code_for_speaking(text):
    # Remove code blocks enclosed in triple backticks from the text for speaking

    text = re.sub(r"```[\s\S]*?```", "Here is a code provided", text)
    text = re.sub(r"流量异常,请尝试更换网络环境","Ask Again",text)
    text = re.sub(r"####","",text)


    
    return text


def speak(text):
    global output_text
    if text is None:
        return
    
    try:
        # Filter out code blocks from the text for speaking
        filtered_text = filter_code_for_speaking(text)

        change_gif(active=True)
        
        engine = pyttsx3.init('sapi5')
        Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
        engine.setProperty('voice', Id)
        
        # Start the typing animation with the full text (including code)
        typing_thread = threading.Thread(target=typing_animation, args=(text, '#38079c', 'Techno: '))
        typing_thread.start()
        
        # Speak the filtered text (without code)
        engine.say(filtered_text)
        engine.runAndWait()
        
        # Wait for the typing effect to complete
        typing_thread.join()
        change_gif(active=False)
        app.update_idletasks()  # Update the GUI
    except Exception as e:
        output_text.insert(END, "ERROR: " + str(e) + "\n")

def get_user_input():
    global output_text
    try:
        change_gif(active=False)
        Q = Listen()
        QL = Q.lower().strip()
        

        
        typing_thread = threading.Thread(target=typing_animation, args=(QL, '#e844fc', 'You: '))
        typing_thread.start()
        typing_thread.join()  # Wait for the typing effect to complete

        return QL
    except Exception as e:
        output_text.insert(END, "ERROR: " + str(e) + "\n")


