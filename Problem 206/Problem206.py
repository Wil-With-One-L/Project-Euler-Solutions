from math import sqrt

def getNextNum(blanks):
  blanks[0] += 1

  for i in range(0, len(blanks)):
    if blanks[i] == 10:
      blanks[i + 1] += 1
      blanks[i] = 0
  
  return blanks

def numString(blanks):
  num = ''
  for i in range(0, 9):
    num += f"{i + 1}"
    num += str(blanks[i])
  num += '0'
  return num

blanks = [0,0,0,0,0,0,0,0,0]

for i in range(0, 999999999):
  s = numString(blanks)
  n = int(s)
  
  if sqrt(n) % 1 == 0:
    print("------========------")
    print(n)
    print(int(sqrt(n)))
    # break

  getNextNum(blanks)

print(numString(blanks))