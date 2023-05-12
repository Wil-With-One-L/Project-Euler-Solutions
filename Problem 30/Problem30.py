nums = []

for i in range(2, 1000000):
  digitSum = 0
  for c in str(i):
    digitSum += int(c) ** 5
  if digitSum == i:
    nums.append(i)

print(nums)

total = 0
for n in nums:
  total += n

print(total)