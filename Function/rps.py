import random
from SpeakGet.Talk import speak, get_user_input

def game_play():
    speak("Let's Play ROCK PAPER SCISSORS !!")
    speak("Sir,you start first choose rock,paper or scissor")
    Me_score = 0
    Com_score = 0
    for _ in range(5):
        choices = ("rock", "paper", "scissor")  # Tuple
        com_choice = random.choice(choices)
        query = get_user_input().lower()
        if query == "rock":
            if com_choice == "rock":
                speak("ROCK")
            elif com_choice == "paper":
                speak("paper")
                Com_score += 1
            else:
                speak("Scissors")
                Me_score += 1
        elif query == "paper":
            if com_choice == "rock":
                speak("ROCK")
                Me_score += 1
            elif com_choice == "paper":
                speak("paper")
            else:
                speak("Scissors")
                Com_score += 1
        elif query == "scissor":
            if com_choice == "rock":
                speak("ROCK")
                Com_score += 1
            elif com_choice == "paper":
                speak("paper")
                Me_score += 1
            else:
                speak("Scissors")
        else:
            speak("Invalid choice. Please choose rock, paper, or scissors.")
    
    

    
    if Me_score > Com_score:
        speak(f"Congratulations! You win! Your score: {Me_score}, My score: {Com_score}")
    elif Me_score < Com_score:
        speak(f"I win! Your score: {Me_score}, My score: {Com_score}")
    else:
        speak(f"It's a tie! Your score: {Me_score}, My score: {Com_score}")