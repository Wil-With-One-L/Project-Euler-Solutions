def factorial(n, memo):
  if n == 0:
    return 1
  if n in memo:
    return memo[n]
  memo[n] = factorial(n - 1, memo) * n
  return memo[n]

def getDigitFactorials(n, memo):
  sum = 0
  n = str(n)
  for c in n:
    sum += factorial(int(c), memo) 
  return sum

memo = dict()
sum = 0
for i in range(3, 50000):
  if i == getDigitFactorials(i, memo):
    sum += i

print(sum)