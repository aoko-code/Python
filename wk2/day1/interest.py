amount = input("enter the amount you want to invest: ")
interest = input("enter the interest rate: ")
amount = float(amount)
interest = float(interest) * .01
for i in range(10):
    amount = amount +(amount * interest)
print("investment after ten years : {:.2f}".format(amount))