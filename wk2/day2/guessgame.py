import random

correctNumber = random.randrange(1, 10)
while True:
    try:
        guess = int(input("guess a number between 1 and 10: "))
        if guess == correctNumber:
            print("you guessed it")
            break
    except ValueError:
        print("please enter a number")
    