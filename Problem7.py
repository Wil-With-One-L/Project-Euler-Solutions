# increase a counter every time a prime is found

primes = []
counter = 0
primeTest = 2

while counter < 10001:
    for i in range(2, primeTest):
        if primeTest % i == 0:
            break
    else:
        primes.append(primeTest)
        counter += 1 # prime found!!
    primeTest += 1

print(primes)
print("------ 10001st-prime------")
print(primes[10000])

#DONE