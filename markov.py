import random

def wordList(filename):
    """takes in a filename for a text file wrapped in quotations, and creates a list
       without any new lines
          Arguments: filename, a text file name like "<example>.txt" 
          Returns: wordList where each element is a word in the original file
    """
    file = open(filename, "r")
    inputList = file.readlines()
    file.close()
    inputList = list(map(lambda x: x.strip("\n"), inputList))
    wordList = inputList[0].split()
    return wordList

def delimiters(wordList, k):
    """delimiters returns wordList updated with k-delimiters following any element 
       with punctuation
           Arguments: wordList, list of strings of words
                      k, number of delimiters '$' wanted d
           Returns: wordList with k delimeters after punctuation
    """
    PUNCTUATION = ['.', '!', '?']
    for i in range(len(wordList)):
        if PUNCTUATION[0] in wordList[i] or PUNCTUATION[1] in wordList[i] 
           or PUNCTUATION[2] in wordList[i]:
             wordList = wordList[:i+1] + ['$']*k + wordList[i+1:]
    return ["$"]*k + wordList

def transitionDictionary(wordList, k):
    """transitionDictionary accepts a list of words in the text and returns a k-th 
       order Markov chain based on that text as a Python dictionary
           Arguments: wordList, list of strings of words
                      k, number of delimiters '$' wanted, the order of the Markov chain
           Returns: wordList with k delimeters after punctuation
    """
    myDictionary = {}
    wordList = delimeters(wordList, k)
    for i in range(len(wordList)-k):
        if wordList[i+k] != "$":
            firstItem = tuple(wordList[i:i+k]) # gives you the first item in list
            if firstItem in myDictionary:
                myDictionary[firstItem].append(wordList[i+k])
            else:
                if wordList[k] != "$":
                    myDictionary[firstItem] = [wordList[i+k]]
                else:
                    myDictionary[firstItem] = [wordList[i]]
    return myDictionary

def gen_from_model(mmodel, numwords):
    """gen_from_model accepts accept a Markov model, determines the order of the 
       Markov model and generates numwords words from it, starting with the 
       all-'$' tuples (using random) based on that transition dictionary
           Arguments: mmodel, Markov model
                      numwords, the number of words to print from that model
           Returns: nothing! It just prints!
    """
    keys = sorted(list(mmodel)) # list of the tuple keys from the markov model
    k = len(keys[0]) # length of tuple
    keyList = ["$"]*k
    nextWord = random.choice(mmodel[keys[0]])
    print(nextWord, end = " ")
    keyList.append(nextWord)
    keyList = keyList[1:]
    myNextKey = tuple(keyList)
    for i in range(numwords - 2):
        nextWord = random.choice(mmodel[myNextKey])
        print(nextWord, end = " ")
        if PUNCTUATION[0] in nextWord or PUNCTUATION[1] in nextWord or PUNCTUATION[2] in nextWord:
            keyList = ["$"]*k
            myNextKey = tuple(keyList)
        else:
            keyList.append(nextWord)
            keyList = keyList[1:]
            myNextKey = tuple(keyList)









