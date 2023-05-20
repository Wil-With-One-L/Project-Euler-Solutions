# Every path in a 20x20 grid will have 40 moves
# Consider each path a list of bools, with 0 being right, and 1 being down
# so right - right - down - right - down - down is written as [001011]
# Every path will have 20 rights and 20 downs

# Find the number of DISTINCT permutations of the string "0000000000000000000011111111111111111111"

def factorial(n, memo):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n in memo:
    return memo[n]
  memo[n] = factorial(n - 1, memo) * n
  return memo[n]

# num of chars = 40
# 0 is repeated 20 times
# 1 is repeated 20 times

memo = dict()
print(factorial(40,memo) / (factorial(20, memo) ** 2))
