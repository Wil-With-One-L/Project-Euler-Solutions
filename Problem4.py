#make a list of all 3 digit products

productSet = set()

for i in range(0, 1000):
    for j in range(0, 1000):
        if (i * j) > 100000: # <---- gets rid of obviously small numbers
            productSet.add(str(i * j))

# print(productSet)

palindromes = []

for i in productSet:
    if i[0] == i[-1] and i[1] == i[-2] and i[2] == i[-3]:
        palindromes.append(int(i))

# print(palindromes)

largest = palindromes[0]

for i in palindromes:
    if i > largest:
        largest = i

print(largest)

#DONE (This one sucked)