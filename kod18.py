class Rectangle:
    width = 0
    height = 0

    def pole(self):
        return self.width * self.height

    def obwod(self):
        return (self.width + self.height) * 2

    def print_obiekt(self):
        print(f'Szerokość: {self.width}, Wysokość: {self.height}, Pole: {self.pole()}, Obwód: {self.obwod()}')


prostokat1 = Rectangle()
prostokat1.width = 5
prostokat1.height = 7
prostokat1.print_obiekt()
