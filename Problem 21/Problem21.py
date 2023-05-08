import math

def getFactors(n):
  factors = []
  i = 1
  while (i * i < n):
      if (n % i == 0):
        factors.append(i)
      i += 1
  for i in range(int(math.sqrt(n)), 0, -1):
      if (n % i == 0):
          factors.append(n // i)
  
  return factors

def factorSum(n):
  sum = 0
  factors = getFactors(n)
  factors.pop() # done to remove the number itself
  for f in factors:
    sum += f
  return sum




factorSums = dict()
sum = 0

for i in range(2, 10000):
  fs = factorSum(i)
  if i not in factorSums:
    factorSums[i] = fs
  if fs not in factorSums:
    fs_b = factorSum(fs)
    factorSums[fs] = fs_b
  if i == factorSums[fs] and i != fs:
    sum += i

print(sum)