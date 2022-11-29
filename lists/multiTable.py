import random
import math

listTable = [[0] * 10 for i in range(10)]
for i in range(1, 10):
    for j in range(1, 10):
        listTable[i][j]= i * j
        

for i in range(1, 10):
    for j in range(1, 10):
        print(listTable[i][j], end=", ")
    print()