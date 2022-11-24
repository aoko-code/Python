#exception handling
while True:
    try:
        number = int(input("please enter a number: "))
        break
    except ValueError:
        print("you did not enter a number")
    except:
        print("an unknown error has occurred")
        
print(number)