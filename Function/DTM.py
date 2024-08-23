import datetime
from SpeakGet.Talk import speak


def get_date():
    speak("Today is {}".format(datetime.datetime.now().strftime('%Y-%m-%d')))

def get_time():
    speak("The current time is {}".format(datetime.datetime.now().strftime('%I:%M %p')))

def get_year():
    speak("The current year is {}".format(datetime.datetime.now().year))