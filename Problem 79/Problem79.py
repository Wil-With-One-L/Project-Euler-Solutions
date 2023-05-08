class OrderList:
  def __init__(self):
    self.befores = set()

def getNumList(filename):
  file = open(filename)
  return file.readlines()

keylogs = getNumList("/Users/wilsonkenny/Desktop/Github-Repositories/Project-Euler-Solutions/Problem 79/p079_keylog.txt")

used_numbers = set()
num_dict = dict()

for k in keylogs:
  first = k[0]
  second = k[1]
  third = k[2]

  if first not in num_dict:
    used_numbers.add(first)
    num_dict[first] = OrderList()

  if second not in num_dict:
    used_numbers.add(second)
    num_dict[second] = OrderList()
  num_dict[second].befores.add(first)

  if third not in num_dict:
    used_numbers.add(third)
    num_dict[third] = OrderList()
  num_dict[third].befores.add(first)
  num_dict[third].befores.add(second)

password = []
for i in range(0, 8):
  password.append(' ')

for n in used_numbers:
  password[len(num_dict[n].befores)] = n

print(password)