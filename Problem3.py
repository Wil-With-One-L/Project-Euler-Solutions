largeNum = 600851475143
testNum = int(input("what number do you want to find the prime factors of?"))
primes = []
factorList = []

# gets factors and adds them to factorList
for i in range(2, testNum + 1):
    if largeNum % i == 0:
        factorList.append(i)

#filters out primes
primeFactorList = []
for i in range(0, len(factorList)): #going through each element in factorList
    for j in range(2, factorList[i]): # multiplying each number by every number between 0 and the number 
        if factorList[i] % j == 0:
            break
    else:
        primeFactorList.append(factorList[i])
        
print("------FACTORS------")
print(factorList)
print("---PRIME-FACTORS---")
print(primeFactorList)

# DONE