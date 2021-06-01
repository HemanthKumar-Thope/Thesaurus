import json
from difflib import get_close_matches

data = json.load(open("data.json"))

#by default the open has read mode

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return ("The word doesn't exist, please check again")
        else:
            return ("We didn't understand your entry")
    else:
        return ("The word Doesn't exist please enter correct word")


word = input("Enter the word you want to find the meaning for : ")

output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
