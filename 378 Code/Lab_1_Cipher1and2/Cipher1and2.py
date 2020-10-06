import string

def main():
    encryptedText1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    encryptedText2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy" 

    # encryptedText 1
    encryptedText1 = str(encryptedText1)
    encryptedText1 = removeSpace(encryptedText1)
    
    alphabet = string.ascii_lowercase
  
    caesarCipher(encryptedText1, alphabet)

    # encryptedText 2
    encryptedText2 = str(encryptedText2)

    encryptedText2 = removeSpace(encryptedText2)

    caesarCipher(encryptedText2, alphabet)
    #closes program after its finished
    exit()


def caesarCipher(encryptedText, alphabet):

    #Dictionary that records tries
    tempDictionary = dict()
    
    for key in range(len(alphabet)): #these lines are used to shift the key and translate the new one.
        translated = ''
        for symbol in encryptedText:
            if symbol in alphabet:
                
                num = alphabet.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(alphabet)
                if num < len(alphabet):
                    translated = translated + alphabet[num]
            else:
                translated = translated + symbol
                #display for tries
        print("Try", str(key+1) ,"- " ,str(translated),)
        var = getFrequency(translated)

        if var is not None:
            tempDictionary.update(var)

    # Sorts the tempDictionary in reverse order
    tempDictionary = sorted(
        tempDictionary.items(), reverse=True, key=lambda x: x[1])
    # Printing sorted dictionary values by most likely score

    print(" - Frequency Chart - ")
    
    for element in tempDictionary:
        print(element[0], " - ", element[1], "matches")
    output = tempDictionary[0]
    # Printing the highest score which is the most likely answer
    print("\n"+"Text based on most common words / combos - ", output, "\n")


#just removes the spaces between the text to improve run time and not produce errors.
def removeSpace(encryptedText):
    encryptedText = encryptedText.replace(" ", "")
    encryptedText = encryptedText.lower()
    
    return encryptedText


def getFrequency(encryptedText):
    #this is the frequency that will be checked
    twoLetter = [ #bi
        "of", "to", "in", "it", "is", "be", "as", "at", "so", "we", "he", "by",
        "or", "on", "do", "if", "me", "my", "an", "no", "us", "am", "th", "er",
        "re", "he", "ed", "nd", "ha", "en", "es", "nt", "ea", "ti", "st", "io",
        "le", "ou", "ar", "as", "de", "rt", "ve", "ss", "ee", "tt", "ff", "ll",
        "mm", "oo"

    ]

    threeLetter = [ #tri
        "the", "and", "for", "are", "but", "not", "you", "all", "any", "can",
        "had", "her", "was", "one", "our", "out", "day", "get", "has", "him",
        "his", "how", "man", "new", "now", "old", "see", "two", "way", "who",
        "boy", "did", "its", "let", "put", "say", "she", "too", "use", "tha",
        "ent", "ion", "tio", "nde", "nce", "edt", "tis", "oft", "sth", "men"
    ]

    fourLetter = [ #quad
        "that", "with", "have", "this", "will", "your", "from", "they", "know",
        "want", "been", "good", "much", "some", "time"
    ]

    counter2 = 0
    counter3 = 0
    counter4 = 0

    #counters used to match the texts

    i = 0
    while i < len(threeLetter):
        if i < len(twoLetter):
            if twoLetter[i] in encryptedText:
                counter2 += 1
        if i < len(threeLetter):
            if threeLetter[i] in encryptedText:
                counter3 += 1
        if i < len(fourLetter):
            if fourLetter[i] in encryptedText:
                counter4 += 1
        i += 1
    
    print("Two Letter matches - ",counter2,"  Three Letter matches - ", counter3,"  Four Letter matches - ", counter4,"\n")
    #displayed matches from the counters above

    totalFreq = counter2 + counter3 + counter4
    #gets frequency so that it can be used in the final display


    if counter2 > 0 or counter3 > 0:  
      #updating for the highest score
        temp_dict = {encryptedText: totalFreq}
        return temp_dict
    else:
        return None

main()

#used https://www3.nd.edu/~busiforc/handouts/cryptography/cryptography%20hints.html to find word Frequency