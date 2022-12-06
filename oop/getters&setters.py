class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("retrieving the height")

        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("please enter numbers for height")


    @property
    def width(self):
        print("retrieving the width")

        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("please enter numbers for width")

    def getArea(self):
        return int(self.__height) * int(self.__width)

def main():
    aSquare = Square()
    height = input("Enter the height: ")
    width = input("Enter the width: ")
    
    aSquare.height = height
    aSquare.width = width

    print("height: ", aSquare.height)
    print("width: ", aSquare.width)

    print("the area is: ", aSquare.getArea())

main()