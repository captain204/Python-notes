from circle import  Circle
from rectangle import  Rectangle


class ShapeDemo():
    @classmethod
    def main(cls, arg):
        width = 2
        length = 3
        radius =10
        rectangle= Rectangle(width,length)
        print("Rectangle with:",width,"Length",length, "Rectangle area",rectangle.area(),rectangle.perimeter())
        circle = Circle(radius)
        print("Circle radius", radius, "Circle area", circle.area,"Circle Perimeter",circle.perimeter())


if __name__ == "__main__":
    import sys
    ShapeDemo.main(sys.argv)