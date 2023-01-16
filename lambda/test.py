def mult_by_2(num):
    return num * 2

times_two = mult_by_2
print(times_two(5))
#pass a function into a function
def do_math(func, num):
    return func(num)

print(do_math(mult_by_2, 9))