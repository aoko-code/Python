name = input("what is your name?? ")

print("hello", name)

num1, operator, num2 = input('enter calculations: ').split()

num1, num2 = int(num1), int(num2)

def sum(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 *num2

def division(num1, num2):
    return num1 / num2
def remainder(num1, num2):
    return num1 % num2
if operator == "+":
    print(" {} {} {} = {} ".format(num1, operator, num2, sum(num1, num2)))
elif operator == "-":
    print(" {} {} {} = {} ".format(num1, operator, num2, difference(num1, num2)))
elif operator == "*":
    print(" {} {} {} = {} ".format(num1, operator, num2, multiplication(num1, num2)))
elif operator == "/":
    print(" {} {} {} = {} ".format(num1, operator, num2, division(num1, num2)))
elif operator == "%":
    print(" {} {} {} = {} ".format(num1, operator, num2, remainder(num1, num2)))
else:
    print("invalid operator")
# use error handling to ensure that onluy positive numbers are entered