
# OH MY GOD THE FIRST SOLUTION WAS RIGHT, I JUST INPUT 11 DIGITS INSTEAD OF 10

def getNums():
    file = open("Problem 13/P13_nums.txt")
    return file.read().split('\n')

nums = getNums()
print(nums)

total = 0
for num in nums:
    num = float(num)
    total += num

print(int(total))