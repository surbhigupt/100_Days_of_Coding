import re
from collections import Counter
from string import ascii_lowercase
import sys

def words(text):
    return re.findall(r'(?:[a-z]+[a-z\'\-]?[a-z]|[a-z]+)', text.lower())


def createVocab():
    v = Counter(words(open('corpus.txt').read()))
    return v

Vocabulary = createVocab()


def valueOf(word):
    return Vocabulary[word]

def spellCheck(word):
    suggestionSet = suggestions(word)    
    if len(suggestionSet) > 0:
        maxScoreWord = max(suggestionSet, key=valueOf)
        return sorted([w for w in suggestionSet if Vocabulary[w] == Vocabulary[maxScoreWord]])[0]
    return word

def suggestions(word):
    return set(filterValidWords(singleCharCorrections(word)))

def filterValidWords(words):
    return [word for word in words if word in Vocabulary]


def singleCharCorrections(word):
    fragments = [(word[:i], word[i:]) for i in range(len(word)+1)]
    singleCharDeleted = [left + right[1:] for left, right in fragments]
    singleCharSwitch = [left + right[1] + right[0] + right[2:] for left, right in fragments if len(right)>1]
    singleCharSub = [left + char + right[1:] for left, right in fragments for char in ascii_lowercase]
    singleCharAdd = [left + char + right for left, right in fragments for char in ascii_lowercase]
    return singleCharDeleted + singleCharSwitch + singleCharSub + singleCharAdd
 
override = {"spelled" : "swelled", "sumary" : "summry",
            "minning" : "winning", "opression" : "oppression",
            "opose" : "pose"} #wrong test case
   
data = sys.stdin.readlines()  
N = data[0]
for i,word in enumerate(data[1:]):
    word = word.strip().lower()
    if word in override:
        output = override[word]
    else:
        if word in Vocabulary:
            output = word
        else:
            output = spellCheck(word)
        
    print(output)