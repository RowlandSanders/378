#sourcecs
#http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
#https://repository.cardiffmet.ac.uk/bitstream/handle/10369/8628/Brown%2C%20Ryan%20James.pdf?sequence=1&isAllowed=y

from math import log10 

class ngram_score(object):
  
    def __init__(self, ngramfile ,sep =' '): #takes in file of n grams and count
      
        self.ngrams = {}
        for line in open(ngramfile):
            key,count = line.split(sep)
            self.ngrams[key] = int(count)

        self.L = len(key)
        self.N = sum(self.ngrams.values())

        
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N) #uses probabilty rather than simple one.
        self.floor = log10(0.01/self.N)

    def score(self,text):    
        
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1): #current computation of the text
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score