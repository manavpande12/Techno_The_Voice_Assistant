import requests
import json
from SpeakGet.Talk import speak, get_user_input


with open('API/news.txt','r') as file:
    apikey = file.read().strip()

def latestnews():
    api_dict = {
        "business": f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={apikey}",
        "entertainment": f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={apikey}",
        "health": f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={apikey}",
        "science": f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={apikey}",
        "sports": f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={apikey}",
        "technology": f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={apikey}"
    }
    
    # Ask for the field until a valid input is provided
    while True:
        speak("Which field news do you want: business, health, technology, sports, entertainment, or science?")
        field = get_user_input().lower()

        url = api_dict.get(field)
        if url:
            break  # Exit the loop if a valid field is provided
        else:
            speak("I didn't understand that.")
    
    speak("Fetching the news.")
    news = requests.get(url).json()
    articles = news["articles"]

    if not articles:
        speak("Sorry, there are no news articles available at the moment.")
        return

    idx = 0
    news_count = 0
    while idx < len(articles):
        article_title = articles[idx]["title"]
        speak(article_title)
        news_count += 1

        # Loop to handle "yes" or "no" response
        while True:
            speak("Would you like to hear the next news? Please say yes or no.")
            response = get_user_input().lower()

            if "no" in response:
                speak("Alright, that's all for the news.")
                break
            elif "yes" in response:
                idx += 1  # Move to the next article
                break  # Exit the inner loop and continue with the next article
            else:
                speak("Sorry, I didn't understand that.")
                # The loop continues asking for a valid response

        if "no" in response:
            break  # Exit the main loop if the user doesn't want more news

    speak(f"We shared {news_count} news articles today.")
