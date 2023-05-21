# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(n):
  n = str(n)
  while len(n) > 1:
    if n[0] != n[-1]:
      return False
    n = n[1:-1]
  return True

nums = []
binNums = []

for n in range(1, 1000000):
  if isPalindrome(n) and isPalindrome(bin(n).replace("0b", "")):
    nums.append(n)
    binNums.append(bin(n).replace("0b", ""))

print(nums)

print(sum(nums))