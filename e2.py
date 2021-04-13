from math import ceil
from copy import copy

class Adres:
    def __init__(self, ulica, numer, miasto):
        self.ulica = ulica
        self.numer = numer
        self.miasto = miasto

    def wyswietl_informacje(self):
        return f'Znajduje sie w miescie: {self.miasto}, przu ulicy {self.ulica} {self.numer}'


class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.semestr = 1
        self.adres = None

    def ustal_adres(self, adres):
        self.adres = adres

    def promuj(self, ilosc_sem=1):
        self.semestr += ilosc_sem

    def pobierz_rok(self):
        return ceil(self.semestr / 2)

    def przedstaw_sie(self):
       return f'Nazywam sie {self.imie} {self.nazwisko}'



akademik = Adres(
    ulica='Akademicka',
    numer=13,
    miasto='Sochaczew'
)

jan = Student('Jan', 'Kowalski')
jan.ustal_adres(akademik)
jacek = copy(jan)
jacek.ustal_adres(akademik)
jacek.imie = 'jacek'

print(jan.przedstaw_sie())
print(jan.adres.wyswietl_informacje())
print ('---' * 30)
print(jacek.przedstaw_sie())
print(jacek.adres.wyswietl_informacje())

