import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getKey():
    key = list(alphabet)
    random.shuffle(key)
    return "".join(key)
    
def encryptor(key, message):
    cipher = ""

    for i in range(len(message)):
        count = 0
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                cipher = cipher + key[count]
                
            else:
                count = count + 1
                
    print("Your cipher:", cipher)
    print("Your randomized key:", key,"\n")


def main_menu():
    print(" - Substitution Encrpytor - ")
    print("1. Choose from preselected 3 messages")
    print("2. Exit")
    print("\n")


def presetMessages():
    print("1. Encrpyt message 1 - He who fights with monsters should... ")
    print("2. Encrpyt message 2 - There is a theory which states that...")
    print("3. Encrpyt message 3 - Whenever I find myself growing grim...")
    print("\n")
         
def getMessage(menuChoice):

    preset1 = "He who fights with monsters should look to it that he himself does not become a monster . And if you gaze long into an abyss , the abyss also gazes into you." 

    preset2 = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here , it will instantly disappear and be replaced by something even more bizarre and inexplicable . There is another theory which states that this has already happened ." 

    preset3 = "Whenever I find myself growing grim about the mouth ; whenever it is a damp , drizzly November in my soul ; whenever I find myself involuntarily pausing before coffin warehouses , and bringing up the rear of every funeral I meet ; and especially whenever my hypos get such an upper hand of me , that it requires a strong moral principle" \
    " to prevent me from deliberately stepping into the street , and methodically knocking people ’s hats off - then , I account it high time to get to sea as soon as I can." 
  
  #gets all of our keys and messages in capitals for consistency 
    if menuChoice == 1: 
        encryptor(getKey(), preset1.upper())
    elif menuChoice == 2:
        encryptor(getKey(), preset2.upper())
    elif menuChoice == 3:
        encryptor(getKey(), preset3.upper())

def main():
    #intial case to end the program later
    case = True
    #while the user hasnt exited the program continue to offer the menu
    while case:
        main_menu()
        menuChoice = int(input("Please enter your choice: "))
        #all the user to encrypt or exit the program

        while menuChoice < 1 or menuChoice > 2:
            menuChoice = int(input("Invalid decision, please choose 1 or 2: "))
            #Error if they dont choose 1 or 2
        if menuChoice == 1:
            presetMessages()
            menuChoice = int(input("Which message would you like to encrpyt? "))
            print("\n")

            while menuChoice < 1 or menuChoice > 3:
                menuChoice = int(input("Invalid decision, please input again: "))
          #error if they dont choose from the preselected message
            if menuChoice == 1:
                getMessage(1)

            elif menuChoice == 2:
                getMessage(2)

            elif menuChoice == 3:
                getMessage(3)

        elif menuChoice == 2:
          print()
          print("Closing program...")
          case = False
main()
