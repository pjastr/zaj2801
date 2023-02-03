class Person:
    wiek = 0
    imie = ''
    nazwisko = ''
    wzrost = 0
    waga = 0

    def przedstaw_sie(self):
        return self.imie + ' ' + self.nazwisko

    def bmi(self):
        return self.waga / self.wzrost**2
