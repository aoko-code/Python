oneTo20 = range(1, 11)

def dbl_num(num):
    return num * 2

print(list(map(dbl_num, oneTo20)))
print(list(map(lambda x: x * 3, oneTo20)))

aList = list(map(lambda x, y: x + y, [1, 3, 6], [1, 2, 3]))
print(aList)