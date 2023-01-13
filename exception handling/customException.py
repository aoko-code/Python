class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dog's name: ")
    if any(char.isdigit() for char in dogName):

        raise DogNameError

except DogNameError:
    print("Your dog's name cant have a number")