sumOfSquares = 0
squareOfSum = 0
difference = 0

for i in range(0, 101):
    sumOfSquares += (i ** 2)
    squareOfSum += i
squareOfSum = squareOfSum ** 2

difference = squareOfSum - sumOfSquares

print(sumOfSquares)
print(squareOfSum)
print("---------")
print(difference)

# DONE