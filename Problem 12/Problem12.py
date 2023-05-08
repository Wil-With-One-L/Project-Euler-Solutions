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

def getTriangleNum(n): # gets the nth triangle number
  sum = 0
  for i in range(1, n + 1):
    sum += i
  return sum

factors = []
n = 1
while len(factors) < 500:
  factors.clear()
  factors = getFactors(getTriangleNum(n))
  n += 1

print(factors)