# get a list of primes between 1 and 2million
import math

def findPrimes(n):
  found = []
  for i in range(0, n + 1):
    found.append(True)
  for i in range(2, math.ceil(math.sqrt(n))):
    if found[i] == True:
      j = i * i
      while j <= n:
        found[j] = False
        j = j + i

  primes = []
  for i in range(2, n):
    if found[i] == True:
      primes.append(i)

  return primes

primesList = findPrimes(2000000)

# print(primesList)

sum = 0
for i in range(0, len(primesList)):
    sum = sum + primesList[i]

print(sum)