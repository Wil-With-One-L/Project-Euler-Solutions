from itertools import permutations

def getPerms(s):
  perms = [''.join(p) for p in permutations(s)]
  return perms

viablePerms = []

for p in getPerms("0123456789"):
  if int(p[1:4]) % 2 != 0:
    continue
  if int(p[2:5]) % 3 != 0:
    continue
  if int(p[3:6]) % 5 != 0:
    continue
  if int(p[4:7]) % 7 != 0:
    continue
  if int(p[5:8]) % 11 != 0:
    continue
  if int(p[6:9]) % 13 != 0:
    continue
  if int(p[7:10]) % 17 != 0:
    continue
  viablePerms.append(p)

print(viablePerms)

total = 0
for p in viablePerms:
  total += int(p)

print(total)