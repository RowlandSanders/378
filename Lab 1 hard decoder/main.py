
print()
print('This uses letter frequency')

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

shuffled = alphabet.copy()

encoded = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"

print()
print("Encoded message: " + encoded)

frequency = list(range(26))
for x in range(0, 26):
  frequency[x]=0

for x in range(0, len(encoded)):
  for y in range(0,26):
    if encoded[x]==alphabet[y]:
      frequency[y] = frequency[y]+1

maxval = max(frequency)

freqlist = alphabet.copy()
n = 0
freqtest = 0

for x in range(0,maxval+1):
  freqtest = maxval-x
  for y in range(0,26):
    if frequency[y] == freqtest:
      freqlist[n] = alphabet[y]
      n=n+1

EnglishFrequency = ['E','I','A','O','I','N','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z']
decoded=""

for x in range(0, len(encoded)):
  if encoded[x] != " ":
    for y in range (0,26):
      if encoded[x] == freqlist[y]:
        decoded = decoded + EnglishFrequency[y]
  else:
    decoded = decoded + " "

print()
print("Decoded message:   "+decoded)

def getChar (message):
  errorFound = 1
  while(errorFound==1):
    char = input(message)
    if len(char) != 1:
      print("Error!")
      errorFound=1
    elif(ord(char)<65) | ((ord(char)>90) & (ord(char) <97)) | (ord(char)>122):
      print("Error!")
      errorFound=1
    else:
      errorFound = 0
  if(ord(char)>96)&(ord(char)<123):
    char = chr(ord(char)-32)    
  
  return char

def replaceChar(inputString):

  print()
  identical = 1
  while(identical==1):
    char1 = getChar("input char to be switched")
    char2 = getChar("input what you wanna replace it with")
    if char1 != char2:
      identical = 0
    else:
      print("Error, the character you entered is exactly the same")

  inputString = inputString.replace(char1, "*")
  inputString = inputString.replace(char2, char1)
  inputString = inputString.replace("*",char2)
  return inputString

  decodedPlus = decoded

  exit = 0
  while(exit==0):
    decodedPlus = replaceChar(decodedPlus)

    print()
    print(decodedPlus)



