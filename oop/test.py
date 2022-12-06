#attributes => fields/ variables
#capabilities => methods/functions
class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
    
    def run(self):
        print("{} the dog runs".format(self.name))
    
    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

def main():
    spot = Dog("spot", 77, 53)

    spot.bark()

    bowser = Dog()
    bowser.eat()

main()