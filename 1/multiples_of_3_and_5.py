total = 0

for i in range(1000):
   if (i % 3 == 0) | (i % 5 == 0):
        total += i

print(total)
