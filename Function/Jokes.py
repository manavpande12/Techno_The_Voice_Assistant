import pyjokes
from SpeakGet.Talk import speak,get_user_input


def tell_joke():
    joke = pyjokes.get_joke()
    speak("Here's a joke for you.")
    speak(joke)
    joke_count=1
    speak("Hope you enjoyed the joke!")
    while True:
        speak("Would you like to hear another joke ? Please say yes or no.")
        response=get_user_input().lower()
        if "yes" in response:
            joke = pyjokes.get_joke()
            speak(joke)
            joke_count+=1
            
        elif "no" in response:
            speak("Alright.")
            break

        else:
            speak("I didn't understand that.")
        
    speak(f"That's all for the jokes. We shared {joke_count} jokes today.")
