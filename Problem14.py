from itertools import chain


chain_length = 0

for num in range(2, 1000000):
    temp_chain_length = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
        temp_chain_length = temp_chain_length + 1
    if temp_chain_length > chain_length:
        chain_length = temp_chain_length

print(chain_length)