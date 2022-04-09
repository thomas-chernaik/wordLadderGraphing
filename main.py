# In this file there will be a function to import the words list,
# generate a graph of connected words, and convert it into a
# javascript array for use in a website. the graph generation only
# needs to run in polynomial time, as it is not used live.
def importWordsToDict(fileName):
    words = {}
    with open(fileName, "r") as myFile:
        for line in myFile:
            words[line.strip()] = []
    return words

def areWordsAdjacent(word1, word2):
    #check the length difference is not more than one
    if abs(len(word1) - len(word2)) > 1:
        return False
    #if the words are the same length then we need to check that only one letter was changed:
    if len(word1) == len(word2):
        count = 0
        for i in range(len(word1)):
            count += word1[i] == word2[i]
        if count > 1:
            return False
        return True
    #make sure the longer word is first
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    pastDiff = False
    for i in range(len(word2)):
        if word1[i] != word2[i - pastDiff]:
            if pastDiff:
                return False
            pastDiff = True
    return True

def getAdajacentWords(dict):
    for word in dict.keys():
        print(".")
        for otherWord in dict.keys():
            if(areWordsAdjacent(word, otherWord)):
                dict[word].append(otherWord)

def main():
    dict = importWordsToDict("words.txt")
    getAdajacentWords(dict)
    print(dict)
if __name__ == "__main__":
    main()