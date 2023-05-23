def fileToNames(filename):
  file = open(filename)
  names = file.read().split(',') 
  file.close()
  for i in range(0, len(names)):
    names[i] = names[i].strip('\"')
  names.sort()
  return names

def makeAlphaDict():
  d = dict()
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  idx = 1
  for letter in alphabet:
    d[letter] = idx
    idx += 1
  return d


names = fileToNames("/Users/wilsonkenny/Desktop/Github-Repositories/Project-Euler-Solutions/Problem 22/p022_names.txt")
alphaDict = makeAlphaDict()

total = 0
nameIdx = 1

for name in names:
  sum = 0
  for char in name:
    sum += alphaDict[char]
  total += (sum * nameIdx)
  nameIdx += 1
  
print(total)

#correct