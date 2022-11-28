def multi_values(num1, num2):
    while (num1, num2) != 0:
        try:
            return (num1 * num2), (num1 / num2)
        except(num1 | num2 == 0):
            print("please enter a positive number")


mult, divide = multi_values(9, 7)
print(mult)