import random 
import math

randlist = ["string", 1, 2, 3, 1235, 76]
oneToTen = list(range(10))
randlist = randlist + oneToTen

print(randlist[0])
print("list length: ", len(randlist))
first3 = randlist[0:3]
for i in first3:
    print("{} : {} ".format(first3.index(i), i))

print(randlist)
print(first3[0] * 3)
print("string" in first3)
print("index of string", first3.index("string"))
print("strings ", first3.count("string"))
