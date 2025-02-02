import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinate: ", self.x, self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        return math.sqrt((self.x-other.x)*(self.x-other.s)+(self.y-other.y)*(self.y-other.y))

