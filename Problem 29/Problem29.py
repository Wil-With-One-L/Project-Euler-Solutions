def findDistinctPowers(x, y):
  powers = set()
  for a in range(x,y + 1):
    for b in range(x,y + 1):
      powers.add(pow(a, b))
  return len(powers)

print(findDistinctPowers(2,100))