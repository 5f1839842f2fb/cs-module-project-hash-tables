def no_dups(s):
    # Your code here
    words = s.split(" ")
    wordList = []
    wordString = ""
    if len(s) == 0:
        return ""
    for word in words:
        if word not in wordList:
            wordList.append(word)
            wordString += " " + word
    wordString = wordString.strip()
    return wordString


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))