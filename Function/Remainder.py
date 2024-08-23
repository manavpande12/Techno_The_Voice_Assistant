from SpeakGet.Talk import speak,get_user_input


def rem_save(query):
    if(query==""):
        speak("What you want me to remember?")
        query = get_user_input().lower()
        query=query.replace("techno","")
        query=query.replace("i want you to remember","")
        query=query.replace("remember that","")
        speak("You told me to remember that " + query)
        with open("Data/Remember.txt", "a") as remember:
            remember.write(query + "\n")
        speak("done")
    else:
        speak("You told me to remember that " + query)
        with open("Data/Remember.txt", "a") as remember:
            remember.write(query + "\n")
        speak("done")

def rem_exe():
    remembered_messages = []
    try:
        with open("Data/Remember.txt", "r") as remember:
            for line in remember:
                remembered_messages.append(line.strip())
    except FileNotFoundError:
        with open("Data/Remember.txt", "w") as remember:
            pass
    if remembered_messages:
        speak("You told me to remember that ")
        for message in remembered_messages:
            speak(message)

        while True:
            speak("Do you want me to forget? please say yes or no")
            query = get_user_input().lower()
            if query == "yes":
                with open("Data/Remember.txt", "w") as remember:
                    remember.write("")
                speak("I've forgotten everything.")
                return False
            elif query=="no":
                speak("okay")
                return False
            else:
                speak("I didn't hear that")
    else:
        speak("I don't remember anything.")