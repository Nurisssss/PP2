class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
a = int(input("Enter lenght: "))
b = int(input("Enter width: "))
rect = Rectangle(a, b)
print(rect.area())
    
