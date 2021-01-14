import math


class Triangle:

    def __init__(self, a, b, c):
        # a,b,c are the sides of triangle
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


class EquiTriangle(Triangle):

    def __init__(self, a):
        b = a
        c = a
        super().__init__(a, b, c)

    def area_equi(self):
        area_equilateral = math.sqrt(3) * pow(self.a, 2) / 4
        return area_equilateral


if __name__ == '__main__':
    a = int(input("1st side of triangle:"))
    b = int(input("2nd side of triangle:"))
    c = int(input("3rd side of triangle:"))
    obj_triangle = Triangle(a, b, c)
    print(obj_triangle.area())
    obj_equitriangle = EquiTriangle(a)
    print(obj_equitriangle.area_equi())
