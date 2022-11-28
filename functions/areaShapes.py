import math
def rectangle_area():
    length = float(input("enter the length: "))
    width = float(input("enter the width: "))
    area = length * width
    print(" the area of the rectangle is : ", area)

def circle_area():
    radius = float(input("enter the redius: "))
    area = math.pi * (math.pow(radius, 2))

    print("The area of the circle is {:.2f}".format(area))

def get_area(shape):
    shape = shape.lower()

    if shape == 'rectangle':
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("please enter reactangle or circle")

def main():
    shape_type = input("enter the shape: ")

    get_area(shape_type)

main()
# parralelograms,  triangles , squares