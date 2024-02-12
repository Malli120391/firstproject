from math import pi
class Circle:
    pi=3.14
    def __init__(self,radius=6):
        self.radius = radius
        self.area = Circle.pi * radius * radius
    def get_circumference(self):
        return 2 * Circle.pi * self.radius
        #return 2 * self.pi * self.radius
Circle_1 = Circle(4)
print(f"The Circumference of circle 1 is: {Circle_1.get_circumference()}")
Circle_2 = Circle(14)
print(f"The Circumference of circle 2 is: {Circle_2.get_circumference()}")
print(f"The area of circle 1 is: {Circle_1.area}")
