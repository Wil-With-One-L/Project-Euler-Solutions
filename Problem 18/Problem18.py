from itertools import product

def makePyramid():
  file = open("/Users/wilsonkenny/Desktop/Github-Repositories/Project-Euler-Solutions/Problem 18/15rowpyramid.txt")
  pyramid = file.readlines()
  for i in range(0, len(pyramid)):
    pyramid[i] = pyramid[i].strip('\n').split(' ')
  return pyramid

def rSubset():
    return list(product([0, 1], repeat=15))

def getMaxPathSum(pyramid):
  maxTotal = 0
  for path in rSubset():
    currRow = 0
    currIdx = 0
    total = 0

    for dir in path:
      total += int(pyramid[currRow][currIdx])
      if dir == 1:
        currIdx += 1
      currRow += 1
    
    maxTotal = max(maxTotal, total)
  return maxTotal

pyramid = makePyramid()
print(getMaxPathSum(pyramid))