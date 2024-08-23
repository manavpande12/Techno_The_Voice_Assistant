import requests
from tkinter import *
import os
import sys

def on_closing(root):
    root.destroy()
    os._exit(0)
    

def show_offline_gui():
    root = Tk()
    root.title("Offline Mode")
    offline_frame = Frame(root)
    offline_frame.pack(fill="both", expand=True)
    label = Label(offline_frame, text="Internet is not available. Please connect to the internet to use the full functionality.")
    label.pack(pady=20)
    button = Button(offline_frame, text="Exit", command=lambda: on_closing(root))
    button.pack(pady=10)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.iconbitmap("Data/icon.ico")
    root.mainloop()

def check_internet():
    try:
        requests.get('https://www.google.com', timeout=3)
        
        return True
    except requests.exceptions.RequestException:
        return False

