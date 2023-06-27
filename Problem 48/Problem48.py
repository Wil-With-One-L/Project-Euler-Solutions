def series(n):
  total = 0
  for i in range(1, n + 1):
    total += i ** i
    print(i)
  return total

print(str(series(1000)))