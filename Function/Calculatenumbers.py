import wolframalpha
from SpeakGet.Talk import speak



def WolfRamAlpha(query):
    with open('API/WolframAlpha.txt','r') as file:
        apikey = file.read().strip()

    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    answer = next(requested.results).text
    return answer


def Calc(query):
    Term = str(query)
    Term = Term.replace("divided by","/")
    Term = Term.replace("times","*")
    Term = Term.replace("into","*")
    Term = Term.replace("divide by","/")
    Term = Term.replace("and","+")
    Term = Term.replace("by","/")
    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        speak("The answer of "+Term+" is: "+result)

    except:
        speak("The value is not answerable")