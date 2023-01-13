num1, num2 = input("enter two values to divide: ").split()
try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {}".format(num1, num2, quotient))
except ZeroDivisionError:
    print("you cant divide by zero")
else:
    print("no exceptions")
finally:
    print("i execute no matter what")