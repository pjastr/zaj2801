class Liczba:
    wartosc = 0

    def dodaj(self, x):
        self.wartosc += x

    def odejmij(self, y):
        self.wartosc -= y


liczba1 = Liczba()
print(liczba1.wartosc)
liczba1.dodaj(4.3)
print(liczba1.wartosc)
