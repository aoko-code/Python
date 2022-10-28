num1, operator, num2 = input('enter calculations: ').split()

num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
difference = num1 - num2
multiplication = num1 *num2
division = num1 / num2
remainder = num1 % num2
if operator == "+":
    print(" {} {} {} = {} ".format(num1, operator, num2, sum))
elif operator == "-":
    print(" {} {} {} = {} ".format(num1, operator num2, difference))
elif operator == "*":
    print(" {} {} {} = {} ".format(num1, operator num2, multiplication))
elif operator == "/":
    print(" {} {} {} = {} ".format(num1, operator num2, division))
elif operator == "%":
    print(" {} {} {} = {} ".format(num1, operator num2, remainder))
else:
    print("invalid operator")
