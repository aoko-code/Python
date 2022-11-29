import random
import math

numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))

numList.insert(5, 10)
numList.sort()
numList.reverse()
for i in numList:
    print(i, end=', ')
print()
