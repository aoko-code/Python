import random 
import math

evenList = [i * 2 for i in range(10)]
for i in evenList:
    print(i)

numList = [7, 2, 3, 4, 5]
listOfValues = [[math.pow(x, 2), math.pow(x, 3), math.pow(x, 4), math.pow(x, 5) ] for x in numList]

for i in listOfValues:
    print(i)
print()