def fib(n, memo):
  if n == 1 or n == 2:
    return 1
  if n in memo:
    return memo[n]
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]

num = 0
i = 1
memo = dict()
while len(str(num)) < 1000:
  num = fib(i, memo)
  i += 1
print(i - 1)