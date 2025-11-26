import random

l = [random.randint(-100,100) for i in range(random.randint(1,20))]
count = 0
for i in l:
    count += 1

print(count, l, len(l))
