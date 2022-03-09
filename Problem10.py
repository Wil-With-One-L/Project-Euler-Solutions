# get a list of primes between 1 and 2million

primesList = []

for i in range(2, 20000): # 200,000 takes a couple minutes, so 2,000,000 would just take forever :/
        for j in range(2, i):   # but its done!
            if i % j == 0:
                break
        else:
            primesList.append(i)

print(primesList)

sum = 0
for i in range(0, len(primesList) - 1):
    sum = sum + primesList[i]

print(sum)