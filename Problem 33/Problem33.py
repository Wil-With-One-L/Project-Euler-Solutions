non_trivials = []

for a in range(10, 100):
  for b in range(a, 100):
    real = a / b

    a_first = a // 10
    b_first = b // 10

    a_last = a % 10
    b_last = b % 10

    if a_first == b_last and b_first != 0: # Ox / xO
      if real == a_last / b_first and a_last != b_first:
        non_trivials.append((a, b))
    elif a_last == b_first and b_last != 0: # xO / Ox
      if real == a_first / b_last and a_first != b_last:
        non_trivials.append((a, b))
  
print(non_trivials)

nume = 1
deno = 1

for p in non_trivials:
  nume *= p[0]
  deno *= p[1]

print(nume / deno)


