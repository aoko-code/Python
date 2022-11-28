def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("Sum: ", sumAll(3,4,5,6,6,3,2,3))