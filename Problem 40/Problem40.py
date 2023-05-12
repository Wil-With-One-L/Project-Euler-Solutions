def getDigits():
  digits = ""
  i = 1
  while len(digits) < 1000002:
    digits = digits + str(i)
    i += 1
  return digits

digits = getDigits()

total = 1

total *= int(digits[1 - 1])
total *= int(digits[10  - 1])
total *= int(digits[100 - 1 ])
total *= int(digits[1000 - 1])
total *= int(digits[10000 - 1])
total *= int(digits[100000 - 1])
total *= int(digits[1000000 - 1])

print(total)