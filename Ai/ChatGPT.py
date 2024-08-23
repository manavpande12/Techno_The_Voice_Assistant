import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
import g4f
from SpeakGet.Talk import speak
from Ai.Cdata import messages

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

def brain(query):
    global messages
    message = "".join(query)
    messages.append({"role": "user", "content": message})

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
            temperature=0.7,  # Lowered temperature slightly for more deterministic responses
            max_tokens=100,
            stop=None,
            no_emoji=True
        )

        content = ""
        for message in response:
            content += message

        speak(content)

    except Exception as e:
        speak("I am not able to answer right now !")

