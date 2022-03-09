sum = 0
a = 1
b = 2
c = 0

while a < 4000000:
    if a % 2 == 0:
        sum = sum + a
        print(a)
    c = a + b
    a = b 
    b = c

print(sum)