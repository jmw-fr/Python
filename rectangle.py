class Rectangle:
#    width = 3
#    height = 2

    def __init__(self, height, width, color = "red") -> None:
        self.height = height
        self.width = width
        self.color = color

    def calculer_surface(self):
        return self.width * self.height

    def empty_method(self):
        pass

    def static_method():
        pass

rect1 = Rectangle(5, 3)
rect2 = Rectangle(1, 1, "blue")
rect3 = Rectangle(1, 1, color="blue")

rect3.color = "red"

rect3.empty_method()

Rectangle.static_method()
