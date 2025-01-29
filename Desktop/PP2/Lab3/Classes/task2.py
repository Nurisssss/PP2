class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length*self.length

a = Shape()
b = Square(int(input()))
print(a.area(), b.area())
