
from Function.DTM import get_date,get_time,get_year
from Function.ClickPic import ClickMe
from Function.YoutubeControl import play,pause,mute,unmute,volumedown,volumeup,fulls,nfulls,sub,unsub,rewind,fast_forward,go_to_beginning,go_to_end
from Function.Schedule import show_schedule,schedule_my_day
from Function.news import latestnews
from Function.rps import game_play
from Function.Jokes import tell_joke


activation_phrases = ["activate"]
names=["techno","hey techno","takeno","tech","take no"]


keyword_synonyms = {
    #Random Call
    "name":["what is your name","name"],
    "greeting":[
        "hello",
        "hi",
        "hey",
        "hi techno",
        "hola",
        "bonjour",
        "hi hi",
        "heyyy",
        "hiiii",
        "hiiiiii",
        "hiiiiiiii",
    ],

    "gesture":[
        "thankyou",
        "thanks",
        "thanks a lot",
        ],

    "function":[
        "what can you do",
        "what power you have",
        "what more things you can do",
        "what are your features",
        "tell me your abilities",
        "what services do you offer",
        "how can you help me"
    ],


    #DTM Call
    "date": ["date", "current date", "what's the date", "tell me the date", "today's date"],
    "time": ["time", "current time", "what's the time", "time now", "tell me the time", "current time please"],
    "year": ["year", "current year", "this year", "what year is it", "tell me the year", "year now"],

    #End Call
    "terminate":["close the program","bye","goodbye"],
    "sleep":["go to sleep","sleep"],

    #Search Call
    "search_google": ["search on google", "google search", "google for", "look up on google"],
    "search_youtube": ["search on youtube", "youtube search", "look up on youtube"],
    "search_wikipedia":["search on wikipedia", "wikipedia search", "look up on wikipedia"],

    #Weather Call
    "weather":["what is the weather", "weather forecast","weather","temperature","humidity","climate","what's the weather like?", "weather forecast", "is it going to rain today?", "temperature today", "weather report", "what is the weather"],
    
    #Calc Call
    "calculate":["calculate","solve"],

    #Take Pic Call
    "TakePic":["take a picture","take a selfie", "take a photo", "take photo"],

    #Open/Close Application Call
    "open":["open the application","open app","open the app","open website","open www.","open www","open application","open the"],
    "close":["close the app","clothes the app","close the application","clothes the application","clothes the app","close app","clothes app","close the","clothes the"],

    #YT Control Call
    "play_yt":["play the music","play the video","play the song","play video","play music", "play song"],
    "pause_yt":["pause the music","pause the video", "pause the song","pause video","pause music", "pause song","stop the music","stop the video","stop the song","stop song","stop video"],
    "mute_yt":["mute the music","mute the video","mute the song","mute video","mute music", "mute song"],
    "unmute_yt":["unmute the music","unmute the video","unmute the song","unmute video","unmute music", "unmute song", "unmute video"],
    "volUp_yt":["volume up","full volume","fast the volume","turn up the volume", "up the volume", "up volume", "increase volume", "increase the volume","volume up"],
    "volD_yt":["volume down","low volume","slow the volume","turn down the volume","down the volume", "down volume", "low the volume", "decrease the volume", "decrease volume", "low the volume"],
    "fulls_yt":["fullscreen the video","full screen the video","turn on full screen","turn on fullscreen"],
    "nfulls_yt":["exit the fullscreen","exit the full screen""exit the fullscreen","exit the video from full screen","turn off full screen","turn off fullscreen", "exit fullscreen", "exit full screen", "close full screen", "close fullscreen"],
    "SubOn_yt":["turn on the caption","turn on the subtitle","subtitle on","caption on", "on caption", "on subtitle"],
    "SubOff_yt":["turn off the caption","turn off the subtitle","subtitle off","caption off", "off caption", "off subtitle"],
    "Rewind_yt": ["rewind", "rewind the video", "rewind video"],
    "FastForward_yt": ["fast forward", "fast forward the video", "skip forward" , "fast forward video"],
    "GoToBeginning_yt": ["go to beginning", "go to start of the video", "go to start the video"],
    "GoToEnd_yt": ["go to end", "go to end of the video", "go to end the video"],

    #Remember Call
    "rem_save":["remember that"],
    "rem_exe":["what do you remember","techno what you remember", "what you remember"],

    #Schedule Call
    "sc_add":["schedule my day"],
    "sc_show":["show my schedule", "show today's schedule"],
    
    #News Call
    "news":["tell me a news","i want hear a news","latest news", "today's latest news", "today's news","tell news"],
    
    #CheckSpeed Call
    "chkint":["check my internet","internet speed" ,"check internet","check internet speed", "check wifi speed","internet speed","check my wifi","check internet","check my wifi"],
    
    #Games Call
    "rps":["game on","lets play","let's play","rock paper scissors", "rock paper scissor"],
    
    #Joke Call
    "joke":["tell me a joke","i want to hear a joke","joke"],

    #GenImg Call
    "gen_img":["generate image of","generate image"],
    }


predefined_questions = {
    "name":"my name is techno",
    "greeting":"Howdy!!!",
    "gesture":"thank you that i am so helpfull you",
    "function":"I can: tell the date/time, take selfies, perform calculations, give daily news, share jokes, set reminders, schedule your day, test internet speed, play games, provide weather updates, surf the web hands-free, control YouTube, open/close apps, generate images, and assist with AI tasks.",

    "date":get_date,
    "time":get_time,
    "year":get_year,

    "TakePic":ClickMe,

    "play_yt":play,
    "pause_yt":pause,
    "mute_yt":mute,
    "unmute_yt":unmute,
    "volUp_yt":volumeup,
    "volD_yt":volumedown,
    "fulls_yt":fulls,
    "nfulls_yt":nfulls,
    "SubOn_yt":sub,
    "SubOff_yt":unsub,
    "Rewind_yt": rewind,
    "FastForward_yt": fast_forward,
    "GoToBeginning_yt": go_to_beginning,
    "GoToEnd_yt": go_to_end,

    "sc_add":schedule_my_day,
    "sc_show":show_schedule,

    "news":latestnews,
    "rps":game_play,
    "joke":tell_joke,


    }

