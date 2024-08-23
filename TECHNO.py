from network.offline import check_internet,show_offline_gui   
import threading
import sys
from Data.reply import activation_phrases,keyword_synonyms,predefined_questions,names
from tkinter import *
from Graphics.win import app,output_text
import os
from Function.WebSearch import search_youtube,search_wikipedia,search_google
from Function.WeatherForecast import get_weather_forecast
from SpeakGet.Talk import get_user_input,speak
from Function.GreetMe import greetMe
import time
from sound.beep import beep
from Ai.ChatGPT import brain

def check_internet_connection():
    while True:
        if not check_internet():
            show_offline_gui()
        time.sleep(3)

def main():
    while True:
        user_input = get_user_input()
        if any(phrase in user_input for phrase in activation_phrases):
            beep()
            greetMe()

            while True:
                user_question = get_user_input()

                if any(phrase in user_question for phrase in names):
                    beep()
                    for keyword, synonyms in keyword_synonyms.items():
                        for synonym in synonyms:
                            if synonym in user_question:
                                            
                                                if keyword == "terminate":
                                                    speak("Goodbye!,i will miss you ")
                                                    os._exit(0)
                                                
                                                elif keyword == "sleep":
                                                    speak("GoodNight!,i will miss you ")
                                                    output_text.insert(END, "Say 'Wake-Up' To Begin\n", 'placeholder')
                                                    output_text.tag_configure('placeholder', foreground='grey')
                                                    while True:
                                                        user_input = get_user_input().lower()
                                                        if "wake up" in user_input:
                                                            speak("Good morning, I'm back online.")
                                                            break
                                                        else:
                                                            time.sleep(1)
                                                    break

                                                elif keyword == "search_google":
                                                    query = user_question.replace(synonym, "").strip()
                                                    for name in names:
                                                        query=query.replace(name,"").strip()
                                                    search_google(query)
                                                    break
                                                elif keyword == "search_youtube":
                                                    query = user_question.replace(synonym, "").strip()
                                                    for name in names:
                                                        query=query.replace(name,"").strip()
                                                    search_youtube(query)
                                                    break
                                                elif keyword == "search_wikipedia":
                                                    query = user_question.replace(synonym, "").strip()
                                                    search_wikipedia(query)
                                                    break 


                                                elif keyword == "weather":
                                                    query = user_question.replace(synonym, "").strip()
                                                    for name in names:
                                                        query=query.replace(name,"").strip()
                                                    try:
                                                        ind = user_question.split().index("in")
                                                        city = " ".join(user_question.split()[ind + 1:])
                                                        get_weather_forecast(city)
                                                    except ValueError:
                                                        speak("Which city would you like to know the weather for?")
                                                        city = get_user_input()
                                                        get_weather_forecast(city)
                                                    break

                                                elif keyword == "calculate":
                                                    query = user_question.replace(synonym, "").strip()
                                                    for name in names:
                                                        query=query.replace(name,"").strip()
                                                    from Function.Calculatenumbers import Calc
                                                    Calc(query)
                                                    break
                            

                            
                            
                                                elif  keyword == "open":
                                                    query = user_question.replace(synonym, "").strip()
                                                    for name in names:
                                                        query=query.replace(name,"").strip()
                                                    from Function.Dictapp import openappweb

                                                    openappweb(query)
                                                    break
                                                elif keyword == "close":
                                                    query = user_question.replace(synonym, "").strip()
                                                    for name in names:
                                                        query=query.replace(name,"").strip()
                                                    from Function.Dictapp import closeappweb
                                                    closeappweb(query)
                                                    break
                                                


                                                elif keyword == "rem_save":
                                                    from Function.Remainder import rem_save
                                                    query = user_question.replace(synonym, "").strip()
                                                    for name in names:
                                                        query=query.replace(name,"").strip()
                                                    rem_save(query)
                                                    break
                                                elif keyword == "rem_exe":
                                                    from Function.Remainder import rem_exe
                                                    rem_exe()
                                                    break
                                                
                                                elif keyword == "gen_img":
                                                     from Function.ImageGen import Generate_Images
                                                     query=user_question.replace(synonym,"").strip()
                                                     for name in names:
                                                        query=query.replace(name,"").strip()
                                                     threading.Thread(target=Generate_Images,args=(query,)).start()
                                                     break
                                                
                                                elif keyword == "chkint":
                                                    from Function.ESpeed import check_internet_speed
                                                    threading.Thread(target=check_internet_speed).start()
                                                    break

                                                else:
                                                    response = predefined_questions[keyword]
                                                    if callable(response):
                                                        speak(response())
                                                    else:
                                                        speak(response)
                                                    break

                        else:
                         continue
                        break
                    else: 
                        query=user_question.lower()
                        brain(query)
                        

                    #else:
                        #speak("Sorry, I didn't understand that.")
                
                else:
                    if not any(name in user_question.lower() for name in names):
                        speak("Say my name then only I will listen to you.")

                    
        else:
            output_text.insert(END, "Say 'Activate' To Begin\n", 'placeholder')
            output_text.tag_configure('placeholder', foreground='grey')

                 
                 


def on_closing():
    app.destroy()
    os._exit(0)
    

def Main():
    t1 = threading.Thread(target=check_internet_connection)
    t2 = threading.Thread(target=beep,daemon=True)
    t3 = threading.Thread(target=main)
    t1.start()
    t2.start()
    t3.start()
    
    
    app.iconbitmap("Data/icon.ico")
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
    sys.exit()
    
Main()