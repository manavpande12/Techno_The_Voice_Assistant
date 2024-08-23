from pygame import mixer
from plyer import notification
from SpeakGet.Talk import speak, get_user_input

def schedule_my_day():
    tasks = []

    speak("Do you want to clear old tasks? Please say YES or NO")
    query = get_user_input().lower()
    
    if "yes" in query:
        try:
            with open("Data/Tasks.txt", "w") as file:
                file.write("")
        except IOError as e:
            speak(f"An error occurred while clearing tasks: {e}")
    elif "no" in query:
        speak("Okay")
    else:
        speak("I didn't hear you. Please say YES or NO.")

    while True:
        speak("Please say the number of tasks.")
        num = get_user_input().lower()
        num = num.replace("one", "1").replace("two", "2").replace("three", "3")
        num = num.replace("four", "4").replace("five", "5")
        
        if num.isdigit():
            no_tasks = int(num)
            if no_tasks <= 5:
                break
            else:
                speak("Please say a number between one and five.")
        else:
            speak("Invalid input. Please say a number between one and five.")

    for i in range(no_tasks):
        speak(f"Please speak task number {i + 1}.")
        task = get_user_input()
        tasks.append(task)
        try:
            with open("Data/Tasks.txt", "a") as file:
                file.write(f"{i + 1}. {task}\n")
        except IOError as e:
            speak(f"An error occurred while saving task {i + 1}: {e}")

    speak("Your schedule has been saved.")

def show_schedule():
    try:
        with open("Data/Tasks.txt", "r") as file:
            content = file.read()
        
    except FileNotFoundError:
        content = "No tasks scheduled yet."
    
    if content.strip() == "":
        speak("No tasks scheduled")
    else:
        mixer.init()
        mixer.music.load("sound/onotify.mp3")
        mixer.music.play()
        speak("Here is your schedule:")
        notification.notify(
            title="My Schedule :-",
            message=content,
            timeout=15,
            app_icon='Data/icon.ico',
            app_name='TECHNO'
        )

    

    


