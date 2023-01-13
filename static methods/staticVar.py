class Dog:
    num_of_dogs = 0

    def __init__(self, name ="unknown"):
        self.name = name

        Dog.num_of_dogs += 1
    @staticmethod
    def getNumOfDogs():
        print("There are {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("Spot")
    doug = Dog("Doug")

    spot.getNumOfDogs()
    doug.getNumOfDogs()

main()