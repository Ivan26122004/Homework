import random
from os import remove

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
first_insert = random.choice(numbers)
n = 0
result = ''
print(first_insert)
for i in range(1, len(numbers) + 1):
    for j in range(1, len(numbers) + 1):
        if first_insert % (i + j) == 0 and i != j:
            if (str(j) + str(i)) in result:
                continue
            result += (str(i) + str(j))
print(result)
