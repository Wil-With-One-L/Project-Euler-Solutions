import string
from itertools import product

def cleanInput(filename):
  file = open(filename)
  line = file.readline().split(',')
  for i in range(0, len(line)):
    line[i] = int(line[i])
  return line

# ============================

nums = cleanInput("Problem 59/0059_cipher.txt")

letters = string.ascii_lowercase
passwords = product(letters, repeat=3)

output_file = open("Problem 59/output.txt", 'w')

i = 0
# PASSWORD IS: exp
# for password in passwords:

total = 0

password = ('e','x','p')
output = ''
idx = 0
for n in nums:
  ascii = n ^ ord(password[idx])
  total += ascii
  let = chr(ascii)
  output += let
  idx = (idx + 1) % 3
output_file.write(output + '\n')

print(total)