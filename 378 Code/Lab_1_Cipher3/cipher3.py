import random
import ngram_score as ns
#This was programmed and run in an online compiler so runtimes may very

#Sources used

#https://inventwithpython.com/hacking/chapter17.html
#http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
#https://repository.cardiffmet.ac.uk/bitstream/handle/10369/8628/Brown%2C%20Ryan%20James.pdf?sequence=1&isAllowed=y

fitness = ns.ngram_score('mixedEnglishgrams.txt')
#collection of ngrams from the internet, uses one that best fits the size of the text.
cipher = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
message = cipher.upper() 

def swap(key):
    
    x = 0
    y = 0
    new = ""

    while(x == y):

        x = random.randint(0,25) #randomly swaps them from the alphabet
        y = random.randint(0,25)

    for i in key: #chooses the index in which the swap occurs
        if key.index(i) == x:
            new += key[y]
        elif key.index(i) == y:
            new += key[x]
        else:
            new += i
    return new
    #returns our new key with swapped char


def replace(input1, input2, message): #this erplaces the current char in the message
    output = ""
    for char in message:
        for i in input1:
            if i == char: #to specify which char we are on
                output+=input2[input1.index(i)]
    return output 
    #returns our replaced text


def decrypt():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    currentBest = -9999999 #infinity / starting best
    amount = 50 
    changes = 2000 #the amount of changes and the amount of computation per iteration

    for i in range(1, amount, 1):
        key = ''.join(random.sample(s, len(s))) #this gives us a random permutation within our key 
        currentBestScore = -9999999 #updates the new best score if found

        for j in range(1, changes, 1):
            newKey = swap(key)
            score = fitness.score(replace(s, newKey, message))
            #a new key with twoi of its letters changed at random

            if score > currentBestScore:
                key = newKey
                currentBestScore = score
            #if the current key is better, it replaces the score

        if currentBestScore > currentBest:
            topKey = key
            currentBest = currentBestScore

        print("Current top key:",topKey, "  Current Score:",currentBest)
    return topKey, currentBest
    #returns the best score and key with it

def main():
    #runs it 3 times to find an answer
    print("This program is running 3 decryptions of the same text")
    #was run and made in an online compiler so runtimes may very

    topKey, currentBest = decrypt()
    topKey2, currentBest2 = decrypt()
    topKey3, currentBest3 = decrypt()

    flag = "ZYGLEBDQHSPMFIKOCNRJUXVWTA"

    #We then get the results of 3 runs
    #Display
    print()
    print(" - Possible Combinations - ")
    print()
    print("Final Key 1:",replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", topKey, flag))
    print(replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", topKey, message))
    print()
    print("Final Key 2:",replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", topKey2, flag))
    print(replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", topKey2, message))
    print()
    print("Final Key 3:",replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", topKey3, flag))
    print(replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", topKey3, message))


main()