import string

def word_count(s):
    # Your code here
    s = s.replace("\n", " ")
    s = s.replace("\r", " ")
    s = s.replace("\t", " ") # surely there's a better way to do this
    wordList = s.lower().split(" ")
    wordDict = {}
    if len(s) > 0:
        for element in wordList:
            stripped = element.strip(string.punctuation)
            if len(stripped) > 0:
                if stripped in wordDict:
                    wordDict[stripped] += 1
                else:
                    wordDict[stripped] = 1
            
    return wordDict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))