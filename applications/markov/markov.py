import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
test = "Banana 1 three banana 1 1 banana 2 2 three banana. \"Start stop.\""
words = words.strip("\n")
words = words.split(" ")

wordDict = {}

for index, word in enumerate(words):
    if word in wordDict:
        if index+1 < len(words):
            wordDict[word].append(words[index+1])
        else:
            wordDict[word] = None
    else:
        if index+1 < len(words):
            wordDict[word] = [words[index+1]]
        else:
            wordDict[word] = None

# print(wordDict)

# TODO: construct 5 random sentences
# Your code here

def markov_sentence(wordDict):
    punctuation = ".?!"
    starters = []
    stoppers = []
    for word in wordDict:
        if word[0].isupper() or (word[0] == "\"" and word[1].isupper()):
            starters.append(word)
        if word[-1] in punctuation or (word[-1] == "\"" and word[-2] in punctuation):
            stoppers.append(word)
    # print(starters)
    # print(stoppers)
    string = ""
    word = random.choice(starters)
    while word not in stoppers:
        string += word + " "
        word = random.choice(wordDict[word])
    string += word + " "
    return string

print(markov_sentence(wordDict))