import math

a = 0
b = 0
c = 0

for i in range(1, 500):
    for j in range(1, 500):
        a = i
        b = j
        c = math.sqrt((a ** 2) + (b ** 2))
        if a < b and b < c and a + b + c == 1000 and c // 1 == c:
            print(a, b, c)
            print(int(a * b * c))
            break