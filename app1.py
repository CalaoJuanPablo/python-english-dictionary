import json
data = json.load(open("data.json"))
from difflib import get_close_matches

sw = 0

while sw == 0:
    def meaning(word):
        word = word.lower()
        closeWord = get_close_matches(word, data.keys())
        
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(closeWord) > 0:
            yn = input("Did you mean %s instead? Y/N " % closeWord[0])
            if yn == "y" or yn == "Y":
                return data[closeWord[0]]
            elif yn == "n" or yn == "N":
                return "The wor does not exist. Check it"
        else:
            return "The word dos not exist. Check it"
    
    word = input("Enter a word: ")
    output = meaning(word)

    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)

    aw = input("Do yow need another word? Y/N ")
    print(aw)
    if aw == "n" or aw == "N":
        print("Thaks for use :). Bye")
        sw = 1
