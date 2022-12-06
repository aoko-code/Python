#1, 1, 2, 3, 5, 8
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result

numWanted = int(input("how many Fibonacci values should be displayed: "))
i = 1
while i < numWanted:
    fibValue = fib(i)
    print(fibValue)
    i +=1

print("All done! ")