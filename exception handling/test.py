try:
    aList = [1, 2, 3]
    print(aList[3])
except IndexError:
    print("Sorry that index doesn't exist")
except:
    print("An Unknnown error occured")