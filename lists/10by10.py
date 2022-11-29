import random
import math

listTable = [[0] * 5 for i in range(5)]
for i in range(5):
    for j in range(5):
        listTable[i][j]= "{} : {}".format(i, j)

for i in range(5):
    for j in range(5):
        print(listTable[i][j], end=" | ")
    print()