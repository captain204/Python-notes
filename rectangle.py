from shape import Shape

class Rectangle(Shape):
    def __init__(self, w=1, l=1):
        self.width = w
        self.length = l

    def setWidth(self,w):
        self.length = w

    def setLength(self,l):
        self.length = l
    def area(self):
        return self.length  * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)