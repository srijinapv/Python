
class Area:
    def __init__(self, length, base, radius,height):
        self.length = length
        self.base = base
        self.radius = radius
        self.height = height

    def area_rect(self):
        area_of_rectangle = self.length * self.base
        return area_of_rectangle

    def area_circle(self):
        area_of_circle = 3.14 * self.radius * self.radius
        return area_of_circle
        
    def area_triangle(self):
        area_of_triangle = 0.5 * self.base * self.height
        return area_of_triangle

if __name__ == '__main__':
    
    length = int(input("Enter length :"))
    base = int(input("Enter base : "))
    radius = int(input("Enter radius :"))
    height = int(input("Enter height :"))

    obj = Area(length, base, radius,height)

    print(obj.area_rect())
    print(obj.area_circle())
    print(obj.area_triangle())