import requests
from SpeakGet.Talk import speak

def get_weather_forecast(city):
    with open('API/openweathermap.txt','r') as file:
        apikey = file.read().strip()
    
    key=apikey
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    try:
        url = f"{weather_url}appid={key}&q={city}"
        js = requests.get(url).json()
        if js["cod"] == "404":
            speak("City Not Found")
        else:
            weather = js.get("main", {})
            temperature = weather.get("temp", 0) - 273.15
            humidity = weather.get("humidity", 0)
            if "weather" in js:
                description = js["weather"][0].get("description", "Unknown")
                weather_response = f"The temperature is {temperature:.2f}°C, humidity is {humidity}%, and the climate is {description}."
                speak(weather_response)
            else:
                speak("Weather information not available.")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather information at the moment.")
