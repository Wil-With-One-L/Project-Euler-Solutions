from itertools import permutations

def getPerms(s):
  perms = [''.join(p) for p in permutations(s)]
  return perms

perms = getPerms("0123456789")

print(perms[999999])
