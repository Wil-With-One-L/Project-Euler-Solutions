def fib(n, memo):
  if n == 1 or n == 2:
    return 1
  if n in memo:
    return memo[n]
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]

def getLast9Digits(n):
  l = []
  for i in range(0, 9):
    l.append(n % 10)
    n = n // 10
  return l

def hasFrontPandigital(n):
  pandigital = [1,2,3,4,5,6,7,8,9]

  n = str(n)
  front = []
  for i in n[0:9]:
    front.append(int(i))
  
  for i in pandigital:
    if i not in front:
      return False
  return True

def hasBackPandigital(n):
  pandigital = [1,2,3,4,5,6,7,8,9]

  
  back = getLast9Digits(n)
  # print(back)

  # print(back)

  for i in pandigital:
    if i not in back:
      return False
  return True

def hasDoublePandigital(n):
  return hasBackPandigital(n) and hasFrontPandigital(n)




memo = dict()

i = 1
while i < 500000:
  num = fib(i, memo)
  if hasDoublePandigital(num):
    print(i)
    break
  
  i += 1