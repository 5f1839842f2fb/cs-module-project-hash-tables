# Your code here

with open("robin.txt") as f:
    words = f.read()

#words = "Banana three banana banana b b b b three banana. \"Start stop.\""
words = words.replace(" ", "99999")
words = words.replace("\n", "99999")
alnumChars = [c for c in words if c.isalnum()]
alnumString = ""
for c in alnumChars:
    alnumString += c
words = alnumString.lower().split("99999")

wordDict = {}
#print(words)
for word in words:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1
#print(wordDict)

output = ""
spacing = 13

wordDict = sorted(wordDict.items()) # turns dict into list of sorted tuples by key name
wordDict = sorted(wordDict, key=lambda key: -key[1]) # sorts list by second '[1]' value of tuple
#print(wordDict)
for word in wordDict:
    output += f'{word[0]}'+ " "* (spacing - len(word[0]))+ "#"* word[1] +"\n"

print(output)