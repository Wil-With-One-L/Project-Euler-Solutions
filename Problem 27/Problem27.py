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

primes = findPrimes(1000)

count = 0
true_a = 0
true_b = 0

for a in range(-1000, 1000):
  for b in range(-1000, 1000):
    currCount = 0
    num = 2
    n = 0
    while num in primes:
      num = (n * n) + (n * a) + b
      currCount += 1
      n += 1
    if count < currCount:
      true_a = a
      true_b = b
    count = max(count, currCount)

print(count)
print(f"a: {true_a}, b: {true_b}")
print(f"a * b:  {(true_a * true_b)}")

