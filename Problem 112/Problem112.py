def isBouncy(n):
  n = str(n)
  increasing = False
  decreasing = False
  for i in range(0, len(n) - 1):
    if n[i] > n[i + 1]:
      increasing = True
      if decreasing:
        return True
    if n[i] < n[i + 1]:
      decreasing = True
      if increasing:
        return True
  return False

bouncies = []
non_bouncies = []

for i in range(100, 2000000):
  if isBouncy(i):
    bouncies.append(i)
  
  if len(bouncies) / i == 0.99:
    print(i)
