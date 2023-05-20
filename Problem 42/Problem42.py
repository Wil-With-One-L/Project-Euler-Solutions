def makeAlphaDict():
  d = dict()
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  idx = 1
  for letter in alphabet:
    d[letter] = idx
    idx += 1
  return d

def getWordList(filename):
  file = open(filename)
  words = file.read()
  words = words.replace('\"', '')
  words = words.split(',')
  return words

def getTriangleNumbers(n):
  tnums = []
  for i in range(0, n):
    tnums.append(int(i * (i + 1) / 2))
  return tnums

def checkTriangleWord(word):
  triangleNums = getTriangleNumbers(100)
  d = makeAlphaDict()
  total = 0
  for c in word:
    total += d[c]
  if total in triangleNums:
    return True
  return False


words = getWordList("/Users/wilsonkenny/Desktop/Github-Repositories/Project-Euler-Solutions/Problem 42/p042_words.txt")

triangleWordCount = 0

for word in words:
  if checkTriangleWord(word):
    triangleWordCount += 1
  
print(triangleWordCount)