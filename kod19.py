class Rectangle:
    width = 0
    height = 0

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width+self.height)

    def print_info(self):
        print(f'Pole: {self.area()}, obwod: {self.perimeter()}')


f1 = Rectangle()
f1.width = 20
f1.height = 30
f1.print_info()
