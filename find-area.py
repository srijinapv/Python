class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        area_circle = 3.14 * self.radius * self.radius
        return area_circle


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        area_rectangle = self.length * self.width
        return area_rectangle


class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def triangle_area(self):
        area_triangle = 0.5 * self.base * self.height
        return area_triangle


if __name__ == '__main__':

    user_choice = int(input("User Choice ( 1 for circle, 2 for rectangle , 3 for triangle):"))

    if user_choice == 1:
        radius = int(input("Enter radius :"))
        obj_circle = Circle(radius)
        print(f"area of circle is {obj_circle.circle_area()}")

    elif user_choice == 2:
        length = int(input("Enter length :"))
        width = int(input("Enter width :"))
        obj_rectangle = Rectangle(length, width)
        print(f"area of rectangle is {obj_rectangle.rectangle_area()}")

    elif user_choice == 3:
        base = int(input("Enter base : "))
        height = int(input("Enter height :"))
        obj_triangle = Triangle(base, height)
        print(f"area of triangle is {obj_triangle.triangle_area()}")

