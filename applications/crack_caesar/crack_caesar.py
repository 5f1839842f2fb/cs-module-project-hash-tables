#### did pair coding in standup as an exercise for most of this
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
# Your code here
# make a dictionary
with open ("ciphertext.txt") as f:
  letters = f.read()
letterDict = {}
for c in letters:
  if c in letterDict:
    letterDict[c] += 1
  else:
    letterDict[c] = 1
# print(letterDict)
# iterate through the dictionary and if it is not a space or punctuation then add to the sum of characters
sum = 0
for c in letterDict:
  if c.isalnum():
    sum += letterDict[c]
# print(sum)
# calculate the frequency of occurences of each character
for c in letterDict:
  letterDict[c] *= 100
  letterDict[c] /= sum 
  letterDict[c] = round(letterDict[c], 2)
print(letterDict)
# compare the cipher to the character values in the letterDict, and whatever pair has the smallest difference is assigned to the character.
cipherDict = {
  "E": 11.53,
  "T": 9.75,
  "A": 8.46,
  "O": 8.08,
  "H": 7.71, 
  "N": 6.73,
  "R": 6.29,
  "I": 5.84,
  "S": 5.56,
  "D": 4.74,
  "L": 3.92,
  "W": 3.08,
  "U": 2.59,
  "G": 2.48,
  "F": 2.42,
  "B": 2.19,
  "M": 2.18,
  "Y": 2.02,
  "C": 1.58,
  "P": 1.08,
  "K": 0.84,
  "V": 0.59,
  "Q": 0.17,
  "J": 0.07,
  "X": 0.07,
  "Z": 0.03
}
decodedDict = {}
for c in letterDict:
  if c.isalnum():
    for d in cipherDict:
      if letterDict[c] == cipherDict[d]:
        #print(c+ " " +d)
        decodedDict[c] = d
        #cipherDict[d] = c
#print(decodedDict)

output = ""
transtable = output.maketrans(decodedDict)
output = letters.translate(transtable)
# for c in cipherDict:
#   output = letters.replace(c, cipherDict[c])
print(output)