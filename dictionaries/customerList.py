#create an array
customers = []

#vreate a loop
while True:
    createEntry = input("Enter Customer(y/n): ")
    createEntry = createEntry[0].lower()

    if createEntry == 'n':
        break
    else:
        fName, lName = input("Enter Customer Name: ").split()
        customers.append({'fName': fName, 'lName': lName})
for cust in customers:
    print(cust['fName'], cust['lName'])
#input y or n
#check to leave loop
