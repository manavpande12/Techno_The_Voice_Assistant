import webbrowser
from SpeakGet.Talk import speak,get_user_input
import pywhatkit
import wikipedia
import webbrowser

def search_youtube(query):
    if(query==""):
        try:
            speak("What You like to search today?")
            response=get_user_input().lower()
            query=response
            web  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("This is what I found for your search!")
            pywhatkit.playonyt(query)
        except:
            speak("I didn't find anything. ")
    else:
        try:
            web  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("This is what I found for your search!")
            pywhatkit.playonyt(query)
        except:
            speak("I didn't find anything. ")

        



def search_google(query):
        import wikipedia as googleScrap
        if(query==""):
            try:
                speak("What You like to search today?")
                response=get_user_input().lower()
                query=response
                pywhatkit.search(query)
                result = googleScrap.summary(query,1)
                speak("This is what I found on google")
                speak(result)
            except:
                speak("No speakable output available")

        else:
            try:
                pywhatkit.search(query)
                result = wikipedia.summary(query,1)
                speak("This is what I found on google")
                speak(result)
            except:
                speak("No speakable output available")






def search_wikipedia(query):
    if(query==""):
        try:
            speak("What You like to search today?")
            response=get_user_input().lower()
            query=response
            results = wikipedia.summary(query,sentences = 2)
            speak("This is what I found on wikipedia")
            speak(results)
        except:
            speak("I didn't find anything. ")
    else:
        try:
            results = wikipedia.summary(query,sentences = 2)
            speak("This is what I found on wikipedia")
            speak(results)
        except:
            speak("I didn't find anything. ")


